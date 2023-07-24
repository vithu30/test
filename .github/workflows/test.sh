#!/bin/sh
zip -r lib.zip commonutils 
export test="$(dirname "$(pwd)")/lib.zip"
echo $test
 export PYTHONPATH=$PYTHONPATH:$test
 echo $PYTHONPATH
 pytest ./api/tests.py
 pytest ./api/tests.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html
