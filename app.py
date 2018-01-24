import twitter
import os

api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'], consumer_secret=os.environ['TWITTER_API_SECRET'], access_token_key=os.environ['TWITTER_ACCESS_TOKEN'], access_token_secret=os.environ['TWITTER_ACCESS_SECRET'])

tweets = api.GetUserTimeline(screen_name="dancinpolkabear", count=200, include_rts=False, trim_user=False, exclude_replies=True)
print(tweets)

while True:
    print(tweets[len(tweets)-1])
    max_id = tweets[len(tweets)-1].id

    new_tweets = api.GetUserTimeline(screen_name="dancinpolkabear", count=200, max_id=max_id, include_rts=False, trim_user=False, exclude_replies=True)
    print(new_tweets)
    tweets += new_tweets
# GetUserTimeline(user_id=None, screen_name="dancingpolkabear", since_id=None, max_id=None, count=200, include_rts=False, trim_user=False, exclude_replies=True)
