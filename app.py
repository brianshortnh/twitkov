"""Rough sample app of Markov Generator"""
import twitter
import os
import markovify

def generate(stuff):
    # Build the model.
    text_model = markovify.Text(" ".join(stuff))

    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(88):
        print(text_model.make_short_sentence(140))

def get_all_tweets(username):
    """Spawns api and gets last 2000 tweets

    @todo check rate limit
    """
    api = new_api()
    tweets = get_tweets(api, username)

    for i in range(0, 300):
        tweets += get_tweets(api, username, since=tweets[len(tweets)-1].id)

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

if __name__ == '__main__':
    data = [tweet.text for tweet in get_all_tweets("realDonaldTrump")]
    generate(data)
