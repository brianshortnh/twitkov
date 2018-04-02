#!/bin/sh

cd $TRAVIS_BUILD_DIR
source twit_ci/bin/activate
pip install zappa
zappa update production
