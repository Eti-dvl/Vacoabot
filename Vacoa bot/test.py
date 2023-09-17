#!/usr/bin/env python
import json
import sys
from twython import Twython

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'
ACCESS_KEY = 'XXX-XXX'
ACCESS_SECRET = 'XXX'

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

