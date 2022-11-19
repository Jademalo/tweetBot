import tweetBot.generator, tweetBot.poster

# Add aliases when this module is imported
tweetBot.ebooksGen = tweetBot.generator.ebooksGen
tweetBot.genreGen = tweetBot.generator.genreGen
tweetBot.variantGen = tweetBot.generator.variantGen

tweetBot.post = tweetBot.poster.post
tweetBot.postTwitter = tweetBot.poster.postTwitter
tweetBot.postMastodon = tweetBot.poster.postMastodon