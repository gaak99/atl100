from __future__ import print_function

from . import __version__

import sys
import os
import ConfigParser
import json
import hy

from fdbhy import FdbOps

ALLCATS=[u'BREAKFAST', u'SMALL PLATES, APPS & SIDES',
         u'SOUPS', u'SALADS', u'BURGERS & SANDWICHES',
         u'PASTA, PIZZA & NOODLES', u'MEATLESS ENTREES',
         u'SOUPS', u'SEAFOOD', u'DESSERTS & SWEETS']

def _get_conf(conf, key):
    path = os.path.expanduser(conf)
    if not os.path.isfile(path):
        sys.exit('error: conf file not found: %s' % conf)
    cf = ConfigParser.RawConfigParser()
    cf.read(path)
    return cf.get('misc', key)

class Atl100():
    def __init__(self, debug, dbname, dbclass):
        self.debug = debug
        #self._debug('__init: {}'.format(self.adminClient))
        self.dbname = dbname
        self.dbclass = dbclass
        key = _get_conf('~/.fdbhyconf', 'admin_key')
        self.fdb = FdbOps(False, dbname, dbclass, key)

    def _debug(self, s):
        if self.debug:
            print(s) # xxx stderr?

    def dbcreat(self):
        self.fdb.dbcreat()

    def dbcreat_class(self):
        self.fdb.dbcreat_class()

    def dbcreat_indexes(self):
        # by restaurant name
        rt= self.fdb.dbcreat_index('dishes100_by_restname',
                             [{"field": ["data", "restname"]}],
                             None,)
        #print('Creat db index w/tags ...')
        rt= self.fdb.dbcreat_index('dishes100_by_tags_with_restname',
                             [{"field": ["data", "tags"]}],
                             [{"field": ["data", "restname"]}]
        )

        # latest dishes by tag
        rt= self.fdb.dbcreat_index('latest_dishes100_by_tag',
                             [{"field": ["data", "tags"]}],
                             [{"field": ["ts"], "reverse": True},
                              {"field": ["data", "restname"]},
                              {"field": ["ref"]}],)
        
        # by dish name
        rt= self.fdb.dbcreat_index('dishes100_by_dishname',
                                   [{"field": ["data", "dishname"]}],
                                   None,)
        #print('Creat db index w/tags ...')
        rt= self.fdb.dbcreat_index('dishes100_by_tags_with_dishname',
                             [{"field": ["data", "tags"]}],
                             [{"field": ["data", "dishname"]}])

        # feedher/noshed bool value by tag
        rt= self.fdb.dbcreat_index('dishes100_by_tags_with_feedher',
                             [{"field": ["data", "tags"]}],
                             [{"field": ["data", "feedher", "noshed"]}])

    def dbinit(self):
        self.dbcreat()
        self.dbcreat_class()
        self.dbcreat_indexes()
        
    def _pr_json_data(self, tags):
        n=0
        for t in tags:
            #print '\nn=', n
            n = n+1
            #print i[0]
            d = t[1]
            for j in d:
                #loop thru map
                name=url=None
                for k,v in j.iteritems():
                    if k == 'name':
                        name=v
                    if k == 'url':
                        url=v
                print('|%s| url=%s'%(name, url))
        
    def _load_json_data(self, filepath):
        with open(filepath, 'rb') as fp:
            tags = json.load(fp)
        if tags:
            print('tags len=%s'%len(tags))
        return tags

    def _upload_one_tag_data(self, tag, dishes):
        for dish in dishes:
            rt = self.fdb.put(dish)
            print(rt)
            rt = self._update_tags(rt['ref'], [tag])
            print(rt)
            
    def _upload_all_dishes(self, tags):
        n=0
        for t in tags:
            curr_tag = t[0]
            print('n=%d tag=%s'%(n,curr_tag))
            n = n+1
            #print i[0]
            d = t[1]
            self._upload_one_tag_data(curr_tag, d)
            for j in d:
                #loop thru map
                name=url=None
                for k,v in j.iteritems():
                    if k == 'name':
                        name=v
                    if k == 'url':
                        url=v
                print('|%s| url=%s'%(name, url))

    def dbload(self, filepath, lolcats):
        tags = self._load_json_data(filepath)
        #self._pr_json_data(tags)
        rt = self._upload_all_dishes(tags)
        
    def get(self, index, string):
        rt = self.fdb.get(index, string)
        print(rt)

    def get_by_tag(self, index, size, tagstr):
        rt = self.fdb.get_by_tag(index, tagstr, size)
        print(rt)

    def get_latest(self, index, size, tagstr):
        rt = self.fdb.get_by_tag(index, tagstr, size)
        print(rt)

    def get_noshed(self, index, size, tagstr):
        rt = self.fdb.get_by_tag(index, tagstr, size)
        print(rt)

    def get_tags(self, index, string):
        rt = self.fdb.get(index, string)
        print(rt['data']['tags'])

    def add_tag(self, index, searchstring, string):
        rt = self.fdb.get(index, searchstring)
        tags = rt['data']['tags']
        # convert to set to avoid dups
        tset = set(tags)
        tset.add(string)
        print(tset)
        print(rt['ref'])
        rt = self._update_tags(rt['ref'], list(tset))
        print(rt)

    def rm_tag(self, index, searchstring, string):
        rt = self.fdb.get(index, searchstring)
        tags = rt['data']['tags']
        # convert to set to avoid dups
        tset = set(tags)
        tset.remove(string)
        print(tset)
        print(rt['ref'])
        rt = self._update_tags(rt['ref'], list(tset))
        print(rt)

    def _update_tags(self, ref, tags):
        #rt = self.fdb.update_tags(ref, tags)
        rt = self.fdb.update_data(ref, 'tags', tags)
        return rt

    def _update_data(self, ref, key, value):
        rt = self.fdb.update_data(ref, key, value)
        return rt

    def noshedit(self, index, searchstring, myrating):
        rt = self.fdb.get(index, searchstring)
        ref = rt['ref']
        feedher = {'noshed':True, 'myrating':myrating}
        rt = self._update_data(ref, 'feedher', feedher)
        print(rt)
        
