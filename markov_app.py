"""Rough sample app of Markov Generator"""
import twitter
import os
import markovify

def generate(tweets, bound):
    generated = []

    # Build the model.
    text_model = markovify.Text(" ".join(tweets))

    # Create a list ofgenerated tweets
    for i in range(0, bound):
        new_tweet = text_model.make_short_sentence(140)
        generated.append(new_tweet)

    return generated

def get_all_tweets(username):
    """Spawns api and gets last 2000 tweets

    @todo check rate limit
    """
    api = new_api()
    tweets = get_tweets(api, username)

    for i in range(0, 10):
        tweets += get_tweets(api, username, since=tweets[len(tweets)-1].id)
#Debug
        print('poop ' + str(i))
        print(username)

    return tweets

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
        count=200,
        include_rts=False,
        trim_user=False,
        exclude_replies=True,
        max_id=since)

def make_tweets(username, num_tweets):
    """Produce an array of generated tweets"""
    data = [tweet.text for tweet in get_all_tweets(username)]
    tweets = generate(data, num_tweets)

    return {
        'username': username,
        'tweets': tweets
    }


def make_tweet_string(username, num_tweets):
    """Produce a valid string of generated tweets"""
    data = [tweet.text for tweet in get_all_tweets(username)]
    tweet_string = "<br/>#############<br/>".join(generate(data, num_tweets))
    return tweet_string

if __name__ == '__main__':
    make_tweet_string("realDonaldTrump", 10)
