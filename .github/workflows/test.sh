#!/bin/sh
zip -r lib.zip commonutils 
export test="$(dirname "$(pwd)")/lib.zip"
echo $test
 export PYTHONPATH=$PYTHONPATH:$test
 pytest ./api/tests.py