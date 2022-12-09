#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweepy
from mastodon import Mastodon
import random
import dotenv
import os
import logging
from str2bool import str2bool



#-------------------------------------------------------------------------------
# Basic Functions
#-------------------------------------------------------------------------------

# Function for returning the keys from environment variables
def getKeysTwitter():
    dotenv.load_dotenv()
    twitterKeys = {
        "TWITTER_CONSUMER_TOKEN": os.getenv("TWITTER_CONSUMER_TOKEN"),
        "TWITTER_CONSUMER_SECRET": os.getenv("TWITTER_CONSUMER_SECRET"),
        "TWITTER_ACCESS_TOKEN": os.getenv("TWITTER_ACCESS_TOKEN"),
        "TWITTER_ACCESS_SECRET": os.getenv("TWITTER_ACCESS_SECRET")
    }
    return twitterKeys;


def getKeysMastodon():
    dotenv.load_dotenv()
    mastodonKeys = {
        "MASTODON_CLIENT_ID": os.getenv("MASTODON_CLIENT_ID"),
        "MASTODON_CLIENT_SECRET": os.getenv("MASTODON_CLIENT_SECRET"),
        "MASTODON_ACCESS_TOKEN": os.getenv("MASTODON_ACCESS_TOKEN"),
        "MASTODON_API_BASE_URL": os.getenv("MASTODON_API_BASE_URL")
    }
    return mastodonKeys;



#-------------------------------------------------------------------------------
# Create API Object
#-------------------------------------------------------------------------------
# Make a tweepy instance using the keys from the provided account variables
def setTwitter(twitterKeys):
    if twitterKeys is None:
        twitterKeys = getKeysTwitter()
    auth = tweepy.OAuthHandler(twitterKeys["TWITTER_CONSUMER_TOKEN"], twitterKeys["TWITTER_CONSUMER_SECRET"])
    auth.set_access_token(twitterKeys["TWITTER_ACCESS_TOKEN"], twitterKeys["TWITTER_ACCESS_SECRET"])
    api = tweepy.API(auth)
    return api

# Make a mastodon instance using the keys from the provided account variables
def setMastodon(mastodonKeys):
    if mastodonKeys is None:
        mastodonKeys = getKeysMastodon()
    api = Mastodon(
        client_id = mastodonKeys["MASTODON_CLIENT_ID"], 
        client_secret = mastodonKeys["MASTODON_CLIENT_SECRET"], 
        access_token = mastodonKeys["MASTODON_ACCESS_TOKEN"], 
        api_base_url = mastodonKeys["MASTODON_API_BASE_URL"]
    )
    return api



#-------------------------------------------------------------------------------
# Post to Network
#-------------------------------------------------------------------------------
def postTwitter(text, keys=None):
    twitter = setTwitter(keys)
    twitter.update_status(status = text)

def postMastodon(text, keys=None):
        mastodon = setMastodon(keys)
        mastodon.toot(text)

    
# Post expects the text to be posted and the frequency at which to post.
# You can disable twitter and mastodon posting by setting twitterPost and mastodonPost to false
# If a key list is specified it will use that, if not it will pull from tweetBot's .env
def post(text, postFreq=1, twitterPost=False, twitterKeys=None, mastodonPost=False, mastodonKeys=None):

    # Fix variable types
    postFreq = int(postFreq) if postFreq is not None else 0
    twitterPost = str2bool(twitterPost) if twitterPost is not None else False
    mastodonPost = str2bool(mastodonPost) if mastodonPost is not None else False

    # Else, generate a random number using it, and if it's 1 then post the tweet
    tweetPostDebug = tootPostDebug = ("No")
    if postFreq != 0 and int(random.randint(1,postFreq)) == 1:
        if twitterPost == True:
            postTwitter(text, twitterKeys)                               # Post the tweet
            tweetPostDebug = ("Yes")
        if mastodonPost == True:
            postMastodon(text, mastodonKeys)                             # Post the toot
            tootPostDebug = ("Yes")

    logging.info("Post to Twitter? - %s", tweetPostDebug)
    logging.info("Post to Mastodon? - %s", tootPostDebug)
