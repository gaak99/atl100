
# Intro
Atl100 is a cli tool to grok Atl's top 100 dishes to try circa 2017 
 
## Status
yo coming soon

## Atl100 Usage
```bash
$ atl100 --help
$ atl100 sub-cmd --help
```


## Quick Start
### One time
* Install

```bash
git clone https://github.com/gaak99/atl100.git
export SUDO=sudo           # set for your env
cd atl100 && $SUDO python setup.py install
export MYBIN=/usr/local/bin # set for your env
```
### As needed

# Tests

```bash
export PYTHONPATH=/tmp/pypath
mkdir /tmp/pypath && python setup.py develop --install-dir /tmp/pypath

# note valid Faunadb auth token needed in ~/.atl100conf
PATH=/tmp/pypath:$PATH bash atl100/tests/atl100tests.sh <new-test-dbname> atl100/tests/test-1cat1dish.json
```




