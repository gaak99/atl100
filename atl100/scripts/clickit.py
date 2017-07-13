
### click module for atl100

import click
from atl100.core import Atl100

from . import __version__

@click.group()
@click.version_option(version=__version__)
@click.option('--debug/--no-debug', default=False,
               envvar='ATL100_DEBUG')
@click.option('--dbname', required=False, default='atl17_100dishes_dev1',
              help='blah')
@click.option('--dbclass', required=False, default='dishes100',
              help='blah')
@click.pass_context
def cli(ctx, debug, dbname, dbclass):
     ctx.obj = Atl100(debug, dbname, dbclass)

# @cli.command(help='Get by rest.')
# @click.argument('rest')
# @click.pass_obj
# def get_by_rest(atl100, rest):
#     atl100.get_by_rest(rest)

# @cli.command(help='Get by name.')
# @click.argument('name')
# @click.pass_obj
# def get_by_name(atl100, name):
#     atl100.get_by_name(name)

@cli.command(help='Search/get one dish.')
@click.option('--index', required=False,
              default='dishes100_by_restname',
              help='Search index. Default is search by restaurant.')
@click.argument('string')
@click.pass_obj
def get(atl100, index, string):
    atl100.get(index, string)

@cli.command(help='Search/get tag list of one dish.')
@click.option('--index', required=False,
              default='dishes100_by_restname',
              help='Search index.')
@click.argument('string')
@click.pass_obj
def get_tags(atl100, index, string):
    atl100.get_tags(index, string)

@cli.command(help='Get all dishes with tag.')
@click.option('--index', required=False,
              default='dishes100_by_tags_with_restname',
              help='Search index.')
@click.option('--size', required=False, default=25,
              help='Search tag return size entries, default=25.')
@click.argument('tagstr')
@click.pass_obj
def get_by_tag(atl100, index, size, tagstr):
    atl100.get_by_tag(index, size, tagstr)

@cli.command(help='Get latest dishes noshed by tag.')
@click.option('--index', required=False,
              default='latest_dishes100_by_tag',
              help='Search index.')
@click.option('--size', required=False, default=25,
              help='Search tag return size entries, default=25.')
@click.argument('tagstr')
@click.pass_obj
def get_latest(atl100, index, size, tagstr):
    atl100.get_latest(index, size, tagstr)

@cli.command(help='Get noshed values by tag.')
@click.option('--index', required=False,
              default='dishes100_by_tags_with_feedher',
              help='Search index.')
@click.option('--size', required=False, default=25,
              help='Search tag return size entries, default=25.')
@click.argument('tagstr')
@click.pass_obj
def get_noshed(atl100, index, size, tagstr):
    atl100.get_latest(index, size, tagstr)

@cli.command(help='Search/add tag to one dish tags list.')
@click.option('--index', required=False,
              default='dishes100_by_restname',
              help='Search field.')
@click.option('--searchstring', required=True,
              help='Search string.')
@click.argument('string')
@click.pass_obj
def add_tag(atl100, index, searchstring, string):
    atl100.add_tag(index, searchstring, string)

@cli.command(help='You noshed it brah!')
@click.option('--index', required=False,
              default='dishes100_by_rest',
              help='Search field.')
@click.option('--searchstring', required=True,
              help='Search string.')
@click.option('--myrating', required=False,
              default=0,
              help='Rate the dish 1-3 NOSHES.')
@click.pass_obj
def INoshedIt(atl100, index, searchstring, myrating):
    atl100.noshedit(index, searchstring, myrating)

@cli.command(help='Search/rm tag of dish.')
@click.option('--index', required=False,
              default='dishes100_by_restname',
              help='Search index.')
@click.option('--searchstring', required=True,
              help='Search string.')
@click.argument('string')
@click.pass_obj
def rm_tag(atl100, index, searchstring, string):
    atl100.rm_tag(index, searchstring, string)

# @cli.command(help='List atl100 dishes sections of meal types.')
# @click.option('--tag', required=False,
#               default='any',
#               help='Search tag')
# @click.pass_obj
# def list_section_tags(atl100):
#     atl100.list_section_tags()

@cli.command(help='Get list of all meal tags of atl100 dishes.')
@click.option('--alldishes/--no-alldishes',
              default=False,
              help='List all dishes of all meal tags.')
@click.pass_obj
def get_mealtags(atl100, alldishes):
    atl100.get_mealtags(alldishes)

@cli.command(help='Creat atl100 dishes db in cloud.')
@click.pass_obj
def dbcreat(atl100):
    atl100.dbcreat()

@cli.command(help='Init db atl100 dishes in cloud.')
@click.pass_obj
def dbinit(atl100):
    atl100.dbinit()

@cli.command(help='Load atl100 dishes raw data into cloud db.')
@click.option('--filepath', required=False,
              default='/home/gb/tmp/atl100.json',
              help='Db raw data local file path.')
@click.option('--lolcats', required=False, default='<all>',
              help='Meal catagories c1,c2,cn')
@click.pass_obj
def dbload(atl100, filepath, lolcats):
    atl100.dbload(filepath, lolcats)

if __name__ == '__main__':
     cli()
