import tweepy
import time
import json
import csv

#from elasticsearch import Elasticsearch

from tweepy import User

consumer_key = '2beMDMlo7GP3J1mJsCZu5CJzy'
consumer_secret = 'gSEL8keHPRwjkIgtD3PWmPnPSE9i4S5uUQhf4ITG4YINvyAPHl'
access_token = '1000023396900536320-BV4LqliYbXEbaYhGd8L0UrrNmtbYXb'
access_token_secret = 'g13Xf7ZQXBkmEiLukJfISRNz8bPHJXPPFY5XV4pHdBgn1'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        # https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile


# this function collects a twitter trending topic request and returns a Twitter object
def get_trends(screen_name):
    api = tweepy.API(auth)
    try:
        trends = api.trends_place(location_id)
    except tweepy.error.TweepError as e:
        trends = json.loads(e.response.text)

    return trends


# this function collects twitter profile tweets and returns Tweet objects
def get_tweet(screen_name):
    try:

        tweets = api.user_timeline(screen_name, count=20)
    except:
        tweets = "broken"

    return tweets


# this function collects twitter  tweets and returns Tweet objects
def get_tweets(query):
    try:

        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]

    return tweets


queries = ["#HanSolo", "\"Nova Scotia\"", "@Windows", "#realDonaldTrump", "#Google", "@SaskMorningNews ‏", "@SaskatoonFire", "#yxe", "@nspowerinc‏", "#Canada", "@VisitNovaScotia" ]

with open('tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id", "user", "created_at", "text"])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            writer.writerow(
                [tweet.id_str, tweet.user.screen_name, tweet.created_at, tweet.text.encode('unicode-escape')])
