ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

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
            taux = achille.princ(username)

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
                                "text":"Histogramme des comptes les plus populaires parmis vos abonnements\nIndice de politisation : {} ".format(taux),
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
                           a = api.update_status(status= "@{} Veuillez suivre le @VacoaBot pour qu il vous envoie un message".format(username), in_reply_to_status_id=d$
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
