#!/bin/sh
pip install virtualenv
virtualenv twit_ci
cd $TRAVIS_BUILD_DIR
source twit_ci/bin/activate
pip install -r requirements.txt
pip install zappa
zappa update production
