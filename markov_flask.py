"""Twitkov Flask App"""
import json
import markov_app as mkv
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    """Main page"""
    return render_template('landing.html')

@app.route('/tweets', methods=['GET'])
def get_tweets():
    """Makes tweets for requested user and return rendered template"""
    twitter_handle = request.args['twitter_handle']
    tweets = mkv.make_tweets(twitter_handle, 30)
    return render_template(
        'results.html',
        username=twitter_handle,
        tweets=tweets['tweets'],
        long_tweets=tweets['long'])

@app.route('/api/<twitter_handle>', methods=['GET'])
def get_api_tweets(twitter_handle):
    """Makes tweets for requested user and return as json"""
    tweets = mkv.make_tweets(twitter_handle, 30)
    return json.dumps(tweets)
