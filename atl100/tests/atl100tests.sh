
### q&d bash script to test 0.1 atl100
#export PYTHONPATH=/tmp/pypathatl100

set -e

dbname=$1
testdata=$2
pydir=/tmp/pypathatl100
atl100=$pydir/atl100
debug='--debug'
dishname='Bread & Butterfly'
cat=BREAKFAST

$atl100 --version

echo atl100test dbinit...
$atl100 $debug --dbname $dbname dbinit

echo
echo atl100test dbload...
$atl100 --dbname $dbname dbload --filepath $testdata

echo
echo atl100test get...
$atl100 --dbname $dbname  $debug get "$dishname"

echo
echo atl100test get...
$atl100 --dbname $dbname  $debug get "$dishname"

echo
echo atl100test get_by_tag...
$atl100 --dbname $dbname  $debug get_by_tag $cat

echo
echo atl100test get_latest...
$atl100 --dbname $dbname  $debug get_latest  $cat

echo
echo atl100test get_noshed...
$atl100 --dbname $dbname  $debug get_noshed $cat

echo
echo atl100test get_tags...
$atl100 --dbname $dbname  $debug get_tags "$dishname"

## add&rm tag
echo
echo atl100test add_tag...
$atl100 --dbname $dbname  $debug add_tag --searchstring "$dishname" "tagmemaybe"

echo
echo atl100test get_tags...
$atl100 --dbname $dbname  $debug get_tags "$dishname"

echo
echo atl100test rm_tag...
$atl100 --dbname $dbname  $debug rm_tag --searchstring "$dishname" "tagmemaybe"

echo
echo atl100test get_tags...
$atl100 --dbname $dbname  $debug get_tags "$dishname"


