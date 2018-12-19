# Tweet-Generator-
Purpose: A program that utilizes changing twitter API’s to grab tweets(data) by using a hashtag or a set of phrases

HLL Used: Python

Information Needed: consumer key, consumer secret, access key, and access secret. You will need these when you connect to the Twitter API while writing code in python. Follow this link, https://developer.twitter.com/content/developer-twitter/en.html,  to request the information needed to proceed.

The Script: 

## The first thing you want to do is import the following files and packages. 

import tweepy

import json

twitter_cred = dict()

# Enter my own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = '***********************'

twitter_cred['CONSUMER_SECRET'] = '***********************'

twitter_cred['ACCESS_KEY'] = '***********************'

twitter_cred['ACCESS_SECRET'] = '***********************'

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

# Mention the hashtag

hashtag = input('Enter the hashtag you want to scrape- ')

for tweet in tweepy.Cursor(api.search, q='#' + hashtag,rpp=100).items(maximum_number_of_tweets_to_be_extracted):
                           
    with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as \
    
        the_file:
        
        the_file.write(str(tweet.text.encode('utf-8')) + '\n')
        

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \n  + ' tweets with hashtag #' + hashtag)

# Get count of likes of each tweet

def get_favourite_count(handle):

    user = api.get_user(handle)
    
    return user.favourits_count
