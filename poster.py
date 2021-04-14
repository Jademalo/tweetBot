#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweepy
import random


#-------------------------------------------------------------------------------
# Twitter related functions
#-------------------------------------------------------------------------------

# Make a tweepy instance using the keys from the provided account variables
def setTwitter(consumer_key, consumer_secret, access_token, access_token_secret):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

# Post a tweet using the text, the account, and optional frequency
def postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreq=1):                                  # postFreq is optional, if not passed it will always be 1 and always post
    twitter = setTwitter(consumer_key, consumer_secret, access_token, access_token_secret)

    # If postFreq is set to 0, don't do anything.
    if postFreq == 0:
        tweetPostDebug = ("No")
    # Else, generate a random number using it, and if it's 1 then post the tweet
    elif int(random.randint(1,postFreq)) == 1:
        tweetPostDebug = ("Yes")
        twitter.update_status(status = tweetText)                               # Update the Status
    else:
        tweetPostDebug = ("No")

    print("Post Tweet? -", tweetPostDebug)
