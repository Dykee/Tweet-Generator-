# In this code you will have significant
# code comments to help you understand it
# Also see my README file for more information.

import tweepy
import json
import unicodedata
twitter_cred = dict()

# Enter my own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'bbPHq0XsUOxfiVzeM5H1yvNfZ'
twitter_cred['CONSUMER_SECRET'] = 'tvtDtZg2yfw09ahl6hoxirLgRz9Ps7V7mHiwsAyQxXm117WEF2'
twitter_cred['ACCESS_KEY'] = '993967710022270979-yDQi1RHSv0FvdHaFtst6uWYcCPVXBha'
twitter_cred['ACCESS_SECRET'] = 'aDJ0nPBTusqMY4z5c01OMi07WUoWDNlfQo7RzZVccnSRr'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)

# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that I want to be extracted.

maximum_number_of_tweets_to_be_extracted = \
    int(input('Enter the number of tweets that you want to extract- '))

# Mention the hash-tag

hashtag = input('Enter the hashtag you want to scrape- ')

# Get count of likes of each tweet

def get_favourite_count(handle):
    user = api.get_user(handle)
    return user.favourits_count

# This
for tweet in tweepy.Cursor(api.search, q='#' + hashtag,
                           rpp=100).items(maximum_number_of_tweets_to_be_extracted):
    with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as \
        the_file:
        the_file.write(str(tweet.text.encode('utf-8')) + '\n')
        unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \
    + ' tweets with hashtag #' + hashtag + str(get_favourite_count))


