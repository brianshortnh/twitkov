<div style="text-align: center">
    <h1 align="center"><a href="https://twitkov.club">Twitkov</a></h1>
    <img align="center" src="/static/markov-portrait-2.jpeg" />
</div>

[![Build Status](https://travis-ci.org/brianshortnh/twitkov.svg?branch=master)](https://travis-ci.org/brianshortnh/twitkov)

An application that harvests a user's Twitter history and spits out a faithful
representation of their entire soul!

## How to run Twitkov

```bash
# Clone
git clone https://github.com/brianshortnh/twitkov.git

# Install requirements:
pip3 install -r requirements.txt

# To run the app, first set your FLASK_APP variable
export FLASK_APP=markov_flask.py

# Now run flask
flask run
```

In your browser navigate to localhost:5000/[username] where [username] is the
Twitter handle you want to generate tweets for.
