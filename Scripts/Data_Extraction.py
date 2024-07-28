import tweepy
import pandas as pd
import os
import sys

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def get_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
    )
    client = tweepy.API(auth)
    return client

def extract_tweets(query, max_tweets):
    client = get_twitter_client()
    tweets = []
    for tweet in tweepy.Cursor(client.search_tweets, q=query, lang="en").items(max_tweets):
        tweets.append([tweet.created_at, tweet.user.screen_name, tweet.text])
    df = pd.DataFrame(tweets, columns=['timestamp', 'user', 'text'])
    return df

df = extract_tweets('python', 100)