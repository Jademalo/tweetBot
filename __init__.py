print(f'Invoking __init__.py for {__name__}')

import tweetBot.main
tweetBot.ebooksTweet = tweetBot.main.ebooksTweet
tweetBot.genreTweet = tweetBot.main.genreTweet
tweetBot.postTweet = tweetBot.main.postTweet
