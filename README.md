
# Intro
Atl100 is a cli tool to grok Atl's top 100 dishes to try circa 2017 
 
## Status
yo just getting started but the basics work mostly

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




