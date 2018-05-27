#!/bin/sh
pip install --upgrade virutalenv
virtualenv --python=python3.6 twit_ci
cd $TRAVIS_BUILD_DIR
source twit_ci/bin/activate
pip install -r requirements.txt
pip install zappa
zappa update production
