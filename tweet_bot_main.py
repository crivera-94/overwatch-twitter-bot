# Overwatch Twitter Bot
#
# Name:
#       Carlos Rivera
# Description:
#       Make a random tweet every minute.
# Details:
#       Inspired by Faisal K

import tweepy
from time import sleep
from overwatch_library import Roster

# get keys and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# use consumer key and consumer secret for login
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# assure connection is secure, set api
auth.secure = True
api = tweepy.API(auth)

# check successful login
# print(str(api.get_user(screen_name='<place @username>')))

# create quote list and print every minute
overwatch_roster = Roster()
quote_list = []
counter = 3
while counter > 0:
    quote_list.append(overwatch_roster.get_message())
    counter -= 1
for quote in quote_list:
    api.update_status(quote)
    sleep(60)
