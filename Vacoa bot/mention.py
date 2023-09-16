#!/usr/bin/env python
import json
import sys
import achille
from twython import Twython
from twython import TwythonStreamer
from twython import TwythonError
from twython import TwythonRateLimitError
from twython import TwythonAuthError
from time import sleep
from threading import Thread
from threading import Timer
import matplotlib.image as mpimg


# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'RbK460gUlUcCkgTixLfmcCCn2'
CONSUMER_SECRET = 'j4lIRpzngxQxNiWnkWnrm5UK0vJQrtcTKsotWKaeCG3BlEkzih'
ACCESS_KEY = '1496183570804662273-J4GfvD1bnpg6hzrsOebdKfIYjt4H89'
ACCESS_SECRET = 'mtsY6xGpn9WOh6L2So87ukiRibDAjhmwrPc8M8vvRSvLk'

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Using our newly created object, utilize the update_status to send in the text passed in through CMD
#api.update_status(status=sys.argv[1])

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))
            user_id = data['user']['id']
            message = "Bonjour {}".format(data['user']['screen_name'])
            achille.princ(username)

            img = open('plot.png','rb')
            response = api.upload_media(media=img,media_type='image/png',media_category='dm_image')
            media_id = response['media_id_string']

            recipient_id = user_id

            params = {
                 "event": {
                      "type":"message_create",
                      "message_create": {
                           "target": {
                                "recipient_id": str(recipient_id),
                           },
                           "message_data": {
                                "text":"Histogramme des comptes les plus populaires parmis vos abonnements",
                                "attachment": {
                                     "type":"media",
                                     "media" : {
                                          "id": str(media_id),
                                     }
                                }
                           }
                      }
                 }
            }
            
            params = json.dumps(params)
            try:
                 response = api.post('direct_messages/events/new',params=params)

            except TwythonError as e:
                 print(e.error_code)
                 if e.error_code == 403 :
                      try:
                           a = api.update_status(status= "@{} Veuillez suivre le @VacoaBot pour qu il vous envoie un message".format(username), in_reply_to_status_id=data['id'])
                      except TwythonError as e2:
                           print(e2)
                 else:
                      print(e)

stream = MyStreamer(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)
stream.statuses.filter(track='@VacoaBot')
