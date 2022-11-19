# TweetBot

This is a hot mess of a twitter bot made specially for my super funky twitter accounts!

https://twitter.com/Genre_Defining  
https://twitter.com/Romantic_ebooks  
https://twitter.com/ulyssebooks


## Usage

Excuse the mess, this is mostly set up so I can just pull a newer list and have it all keep running.  
`JadeBots.py` and `JadeBotsRun.py` are my personal implementations of tweetBot for the three bots that I run.

tweetBot is a module with two main components - Generate and Post.  
It uses [Tweepy](https://www.tweepy.org/) to post to twitter, so that is absolutely required.
If you import it, you get three main functions.

```python
postTweet(tweetText, account, postFreq=1)
ebooksGen(file, maxLength=100, minLength=30)
genreGen(gameFile, genreFile, genreExtraFile, altPostFreq=0, altGenreGameFreq=0, altGenreExtraFreq=0)
```


### postTweet()

Post tweet is relatively simple.  
`tweetText` is the text to be tweeted, `account` is a string name of your account as defined in keys.py, and `postFreq` is an optional argument to disable posting with 0, or have a 1 in x chance of happening.


### ebooksGen()

This returns a string using the ebooks generator.  
`file` is a string path to a file, which it loads. It then chops out a random piece in the middle of it with an optional max and min length for the tweet.


### genreGen()

This is maybe a bit needlessly configurable, but it's still fairly simple to use.
It returns a string using the Genre Defining generator, as well as some extra debug info. Check `JadeBots.py` to see all of that.
The three main files are loaded with `gameFile`, `genreFile`, and `genreExtraFile` which are all just string paths to files.  
There are three main variables - `altPostFreq` which is how often it uses the alternate "what if" output, `altGenreGameFreq` which is how often it uses the "game-like" variant for genres, and `altGenreExtraFreq` which is how often it takes from the extra list of rarer genres.
All of these variables can be disabled with 0, or have a 1 in x chance of happening.  


### Examples

If you wish to post to multiple accounts with the same execution, you can pass account environment variables through `tweetBot.post()`. If these aren't passed, the poster will pull the necessary environment variables directly.
```python
def postRomanticsEbooks():

    text = "This is a test"

    dotenv.load_dotenv()
    mastodonKeys = [
        os.getenv("ACC1_MASTODON_CLIENT_ID"),
        os.getenv("ACC1_MASTODON_CLIENT_SECRET"),
        os.getenv("ACC1_MASTODON_ACCESS_TOKEN"),
        os.getenv("ACC1_MASTODON_API_BASE_URL")
    ]

    tweetBot.post(text, twitterPost=False, mastodonKeys=mastodonKeys)
```