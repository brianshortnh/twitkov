#Flask quickstart
import nathan
from flask import Flask, request, json
app = Flask(__name__)

@app.route('/<twitter_handle>')
def do_the_thing(twitter_handle):
    data = [tweet.text for tweet in nathan.get_all_tweets(twitter_handle)]
    return nathan.generate(data)
