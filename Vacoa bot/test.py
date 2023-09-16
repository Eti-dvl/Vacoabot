#!/usr/bin/env python
import json
import sys
from twython import Twython

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'RbK460gUlUcCkgTixLfmcCCn2'
CONSUMER_SECRET = 'j4lIRpzngxQxNiWnkWnrm5UK0vJQrtcTKsotWKaeCG3BlEkzih'
ACCESS_KEY = '1496183570804662273-J4GfvD1bnpg6hzrsOebdKfIYjt4H89'
ACCESS_SECRET = 'mtsY6xGpn9WOh6L2So87ukiRibDAjhmwrPc8M8vvRSvLk'

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Using our newly created object, utilize the update_status to send in the text passed in through CMD
#api.update_status(status=sys.argv[1])

result = api.show_user(screen_name=sys.argv[1])

api.send_direct_message(event = {"type": "message_create",
    "message_create":{"target": {"recipient_id": result['id']},
    "message_data":
    {"text": sys.argv[2]}}})
#print("Tweeted : "+ sys.argv[1])

