from textblob import TextBlob
import tweepy

consumer_key = "DS4zhZLQ513LsYC4OwZVuiQLO"
consumer_secret = "ZS3Vr889R1MnbLYPSShwJ4zVrjgCGTJcAwrBFZ5UggPi8CJYXG"

access_token = "974884027701366784-Cc1GzoYShMRmhIcBIwIIYvhS1sbZFFc"
access_token_secret = "Fn0WfasBOS0SFf1nLliTv7XxZXhHmc8c9KlTpgic9VgXV"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
