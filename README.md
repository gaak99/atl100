
# Intro
Atl100 is a basic CLI tool -- written in Python and Hy -- to populate -- using the FaunaDB API -- Atlanta's top 100 dishes to try circa 2017.

The point of this is

1. give the FaunaDB API (and freemium svc) a try
2. maybe use the svc in a future project
 
## Status
Point 1 above is finished and works pretty good (though def unpolished).

## Hy (with/instead of Python)
The functional nature of the FaunaDB API is pretty groovy and was one of my main attractions to this svc.

While working thru the db tutorial I realized this may be a perfect fit for Hy to improve the code: https://github.com/gaak99/faunadb-hylisp

## Quick Start
### One time
* Install
```bash
git clone https://github.com/gaak99/atl100.git
# may need sudo for install
cd atl100 && python setup.py install
```

* Add your Faunadb admin key to ~/.atl100conf
```
[misc]
admin_key=<myadminkey>
```

### Basic Usage
#### Once per db
```bash
$ atl100 --dbname <dbname> dbinit
$ atl100 --dbname <dbname> dbload --filepath $ATL100/atl100/data/atl100-data.json
# q&d verify db
$ atl100 --dbname <dbname> get_mealtags --alldishes
```

#### Apply as needed
```bash
$ atl100 --help
$ atl100 sub-cmd --help
```

# Tests
```bash
export PYTHONPATH=/tmp/pypath
mkdir /tmp/pypath && python setup.py develop --install-dir /tmp/pypath

# note valid Faunadb auth token needed in ~/.atl100conf
PATH=/tmp/pypath:$PATH bash atl100/tests/atl100tests.sh <new-test-dbname> atl100/tests/test-1cat1dish.json
```

# Refs

* https://faunadb.com
* https://everipedia.org/wiki/fauna-faunadb/
* https://dbmsmusings.blogspot.com/2017/04/distributed-consistency-at-scale.html
* https://github.com/hylang/hy

# Future Features
* Mobile

## Next Level Sh*te
* http://www.techradar.com/news/how-three-words-could-change-the-way-we-navigate-the-globe
