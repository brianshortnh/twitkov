#Flask quickstart
import markov_app as mkv
from flask import Flask, request, url_for, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/<twitter_handle>', methods=['GET'])
#def make_one_tweet(twitter_handle):
#    tweet = mkv.make_tweet_string(twitter_handle, 1)
#    return "New tweet for {0}:\n{1}".format(twitter_handle, tweet)

def make_five_tweets(twitter_handle):
    tweets = mkv.make_tweet_string(twitter_handle, 5)
    return "New tweets for {0}:<br/>{1}".format(twitter_handle, tweets)
