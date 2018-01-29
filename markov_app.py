"""Rough sample app of Markov Generator"""
import os
import twitter
import markovify

TWEET_LIMIT = 200

def generate(text_model, size, bound):
    """Makes 140 character tweets"""
    return [text_model.make_short_sentence(size) for i in range(0, bound)]

def get_all_tweets(username):
    """Spawns api and gets last 2000 tweets"""
    api = new_api()
    tweets = get_tweets(api, username)

    for i in range(0, 20):
        tweets += get_tweets(api, username, since=tweets[len(tweets)-1].id)

    return tweets

def make_tweets(username, num_tweets):
    """Produce an array of generated tweets"""
    data = [tweet.text for tweet in get_all_tweets(username)]
    model = make_markov_model(data)

    return {
        'username': username,
        'tweets': generate(model, 140, num_tweets),
        'long': generate(model, 240, 2),
    }

def make_tweet_string(username, num_tweets):
    """Produce a valid string of generated tweets"""
    data = [tweet.text for tweet in get_all_tweets(username)]
    tweet_string = "<br/>#############<br/>".join(generate(data, 140, num_tweets))
    return tweet_string

# Utility
def new_api():
    """Wrapper around spawning twitter api"""
    return twitter.Api(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_SECRET'])

def get_tweets(api, username, since=None):
    """Wrapper around api request"""
    return api.GetUserTimeline(
        screen_name=username,
        count=TWEET_LIMIT,
        include_rts=False,
        trim_user=False,
        exclude_replies=True,
        max_id=since)

def make_markov_model(tweets):
    """Wrapper around making Markov Chain"""
    return markovify.Text(" ".join(tweets))

if __name__ == '__main__':
    make_tweet_string("realDonaldTrump", 10)
