#-------------------------------------------------------------------------------
# This file adds a function to return keys so that my keys aren't shared on GitHub
# Rename this file to keys.py, and add your own names and keys


#-------------------------------------------------------------------------------
# Listing the names of the different accounts
#-------------------------------------------------------------------------------
acc1 = "accountOne"
acc2 = "accountTwo"
acc3 = "accountThree"


#-------------------------------------------------------------------------------
# Function for returning the keys
#-------------------------------------------------------------------------------
def returnKeys(account):
    if account == acc1:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

    elif account == acc2:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

    elif account == acc3:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

    else:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

    return consumer_key, consumer_secret, access_token, access_token_secret;
