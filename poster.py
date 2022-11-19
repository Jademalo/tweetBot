#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweepy
from mastodon import Mastodon
import random
import dotenv
import os



#-------------------------------------------------------------------------------
# Function for returning the keys from environment variables
#-------------------------------------------------------------------------------
def getKeysTwitter():
    dotenv.load_dotenv()
    twitterKeys = [
        os.getenv("TWITTER_CONSUMER_TOKEN"),
        os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET")
    ]
    return twitterKeys;


def getKeysMastodon():
    dotenv.load_dotenv()
    mastodonKeys = [
        os.getenv("MASTODON_CLIENT_ID"),
        os.getenv("MASTODON_CLIENT_SECRET"),
        os.getenv("MASTODON_ACCESS_TOKEN"),
        os.getenv("MASTODON_API_BASE_URL")
    ]
    return mastodonKeys;



#-------------------------------------------------------------------------------
# Create API Object
#-------------------------------------------------------------------------------
# Make a tweepy instance using the keys from the provided account variables
def setTwitter(twitterKeys):
    if twitterKeys is None:
        twitterKeys = getKeysTwitter()
    auth = tweepy.OAuthHandler(twitterKeys[0], twitterKeys[1])
    auth.set_access_token(twitterKeys[2], twitterKeys[3])
    api = tweepy.API(auth)
    return api

# Make a mastodon instance using the keys from the provided account variables
def setMastodon(mastodonKeys):
    if mastodonKeys is None:
        mastodonKeys = getKeysMastodon()
    api = Mastodon(
        client_id = mastodonKeys[0], 
        client_secret = mastodonKeys[1], 
        access_token = mastodonKeys[2], 
        api_base_url = mastodonKeys[3]
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
def post(text, postFreq=1, twitterPost=True, twitterKeys=None, mastodonPost=True, mastodonKeys=None):
    # If postFreq is set to 0, don't do anything.
    if postFreq == 0:
        tweetPostDebug = ("No")
    # Else, generate a random number using it, and if it's 1 then post the tweet
    elif int(random.randint(1,postFreq)) == 1:
        tweetPostDebug = ("Yes")
        if twitterPost == True:
            postTwitter(text, twitterKeys)                               # Post the tweet
        if mastodonPost == True:
            postMastodon(text, mastodonKeys)                             # Post the toot
    else:
        tweetPostDebug = ("No")

    print("Post? -", tweetPostDebug)
