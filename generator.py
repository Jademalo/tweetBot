#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import random


#-------------------------------------------------------------------------------
# Basic Functions
#-------------------------------------------------------------------------------

# Convert a file to a list
def fileToList(fileName):
    fileRaw = open(fileName, "r", encoding="utf-8")
    fileString = fileRaw.read()
    fileList = fileString.split("\n")
    return list(filter(None, fileList))

# Convert a file to a string
def fileToString(fileName):
    fileRaw = open(fileName, "r",  encoding="utf-8")
    return fileRaw.read()

# Get a random int between 1 and the passed value
def randomInt(max):
    return int(random.randint(1,max))

# Get a random entry from a list
def randomList(list):
    listNumber = len(list)                                                      # Finding the length of the list
    return list[randomInt(listNumber) - 1]                                      # Generating a random value from that list, -1 since 0 is a value # Returning the specific value from the list based on the number generated



#-------------------------------------------------------------------------------
# Tweet generation functions
#-------------------------------------------------------------------------------

# Return a string of a random length and random amount of a text file
def ebooksGen(file, maxLength=100, minLength=30):
    # Prevent a tweet being too long
    if maxLength > 280:
        maxLength = 280
    # Read File into a string
    fileString = fileToString(file)
    # Get the length of the tweet
    tweetLength = int(random.randint(minLength,maxLength))
    # Find a point in the string to start
    tweetStart = int(random.random()*(len(fileString)-280))
    # Shorten the string, then split it into individual words
    workingTweet = fileString[tweetStart:tweetStart+tweetLength].split(" ")
    # Chop off the first word
    workingTweet = workingTweet[1:]
    # Chop off the last word
    workingTweet = workingTweet[:-1]
    # Join the tweet back together
    workingTweet = " ".join(workingTweet)
    # Remove linebreaks
    finalTweet = workingTweet.replace('\n', ' ').replace('\r', '')
    # Return the final tweet
    return finalTweet


# Return a string compositied from various files
def genreGen(gameFile, genreFile, genreExtraFile, altPostFreq=0, altGenreGameFreq=0, altGenreExtraFreq=0):

    # Convert the files into lists
    gameList = fileToList(gameFile)
    genreList = fileToList(genreFile)
    genreExtraList = fileToList(genreExtraFile)
    # Get a random game from the game list
    gameText = randomList(gameList)


    # Set debug info
    altGenreGameDebug = ("No")
    altGenreExtraDebug = ("No")

    # If a value has been passed for either of the alt genre variables
    if altGenreGameFreq != 0 or altGenreExtraFreq != 0:
        # If genre game has been set and the random variable is 1, set to mode 2
        if altGenreGameFreq != 0:
            if randomInt(altGenreGameFreq) == 1:
                genreMode = 2
            else:
                genreMode = 0
        # Else, if genre extra has been set and the random variable is 1, set to mode 2
        elif altGenreExtraFreq != 0:
            if randomInt(altGenreExtraFreq) == 1:
                genreMode = 1
            else:
                genreMode = 0
    # Else, if no values have been passed then default to mode 0
    else:
        genreMode = 0

    # If the mode is set to standard, pick a string from the genre list
    if genreMode == 0:
        genreText = randomList(genreList)
    # Else, if the mode is set to extra, pick a string from the genre extra list
    elif genreMode == 1:
        altGenreExtraDebug = ("Yes")
        genreText = randomList(genreExtraList)
    # Else, if the mode is set to game as genre, pick a string from the game list and add like
    elif genreMode == 2:
        altGenreGameDebug = ("Yes")
        genreText = randomList(gameList)
        # If the last character is a ".", remove it
        if genreText[-1:] == ("."):
            genreText = genreText[:-1]
        genreText = "".join((genreText, "like"))                                # There are two brackets because the first set makes a string from the two values, and second joins them


    # Work out of "a" or "an" is needed
    if genreText[0] == ("a") or genreText[0] == ("e") or genreText[0] == ("i") or genreText[0] == ("o") or genreText[0] == ("u") or genreText[0] == ("A") or genreText[0] == ("E") or genreText[0] == ("I") or genreText[0] == ("O") or genreText[0] == ("U"):
        connectText = (" an ")
    else:
        connectText = (" a ")


    # Logic to decide if alternate format
    altPost = randomInt(altPostFreq)
    altPostDebug = ("No")

    # If statement to change the format of the question, then composite the final tweet
    if altPost == 1:
        altPostDebug = ("Yes")
        workingTweet = ("What if ", gameText, " was", connectText, genreText, "?")
    else:
        workingTweet = ("Is ", gameText, connectText, genreText, "?")

    tweetText = "".join(workingTweet)

    return tweetText, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug


# Return a string composited from various files, with a random number of elements
def variantGen(nameFile, prefixFile, suffixFile):

    # Convert the files into lists
    nameList = fileToList(nameFile)
    prefixList = fileToList(prefixFile)
    suffixList = fileToList(suffixFile)

    prefixRate = randomInt(100)
    suffixRate = randomInt(100)

    # Get a random name from the name list
    nameText = randomList(nameList)
    # Get a random prefix from the prefix list
    prefixText = randomList(prefixList)
    # If the random number is correct, add an additional prefix
    if prefixRate >= 60:
        prefixExtraDebug = ("Yes")
        prefixExtraText = randomList(prefixList)
    else:
        prefixExtraDebug = ("No")
        prefixExtraText = ""
    # If the random number is correct, add a suffix
    if suffixRate >= 90:
        suffixDebug = ("Yes")
        suffixText = randomList(suffixList)
    else:
        suffixDebug = ("No")
        suffixText = ""


    # Composite final tweet
    if prefixRate >= 60:
        workingTweet = (prefixExtraText," ",prefixText," ",nameText," ",suffixText)
    else:
        workingTweet = (prefixText," ",nameText," ",suffixText)

    tweetText = "".join(workingTweet)

    return tweetText, nameText, prefixText, suffixText, prefixExtraText, prefixExtraDebug, suffixDebug
