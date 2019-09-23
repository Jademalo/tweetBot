#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import keys
import tweepy
import random


#-------------------------------------------------------------------------------
# Twitter related functions
#-------------------------------------------------------------------------------

# Make a tweepy instance using the keys from the provided account variable
def setTwitter(account):
    consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

# Post a tweet using the text, the account, and optional frequency
def postTweet(tweetText, account, postFreq=1):                                  # postFreq is optional, if not passed it will always be 1 and always post
    twitter = setTwitter(account)

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
