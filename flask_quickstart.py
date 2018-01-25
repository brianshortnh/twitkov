#Flask quickstart
import nathan
from flask import Flask, request
app = Flask(__name__)

@app.route('/<twitter_handle>')
def do_the_thing(twitter_handle):
    return ', '.join([tweet.text for tweet in
                      nathan.get_all_tweets(twitter_handle)])
