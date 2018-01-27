<h1 align="center"><a href="http://twitkov.club">twitkov</a></h1>
<img align="center" src="/static/markov-portrait.jpg" />

An application that harvests a user's Twitter history and spits out a faithful
representation of their entire soul!

## How to run twitkov
Clone the repo:
`git clone https://github.com/brianshortnh/twitkov.git` or
`git clone git@github.com:brianshortnh/twitkov.git`

Install requirements:
`pip3 install -r requirements.txt`

To run the app, first set your FLASK_APP variable, then run flask:
```bash
export FLASK_APP=markov_flask.py
flask run
```

In your browser navigate to localhost:5000/[username] where [username] is the
Twitter handle you want to generate tweets for.
