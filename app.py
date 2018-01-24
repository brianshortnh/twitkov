import twitter
import os


def get_all_tweets(username):
    api = new_api()
    tweets = get_tweets(api, username)

    for i in range(0, 10):
        tweets += get_tweets(api, username, since=tweets[len(tweets)-1].id)

    return tweets

def new_api():
    return twitter.Api(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_SECRET'])

def get_tweets(api, username, since=None):
    return api.GetUserTimeline(
        screen_name=username,
        count=200,
        include_rts=False,
        trim_user=False,
        exclude_replies=True,
        max_id=since)

print(get_all_tweets("dancinpolkabear"))

# GetUserTimeline(user_id=None, screen_name="dancingpolkabear", since_id=None, max_id=None, count=200, include_rts=False, trim_user=False, exclude_replies=True)
