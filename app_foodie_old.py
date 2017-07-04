import os, sys
from flask import Flask, request
import json
from random import shuffle
import pprint
import utils_foodie
#from pymessenger import Bot

app= Flask(__name__)

FB_ACCESS_TOKEN = "EAADEBIVRjEIBAEfiwMcJXG2AHFyoHlNaCAwQbI9lBp8zZAVJ4npAeL4bQIYVmaJQK0H8Ogq8RccKqe3z9OwHCdrv8AiLbuXKcCeOYUIqOD65zZBvbmM7eZB06jwg2n9EZBGBgGZAOjKvCcFCI8q1UtpJk6YmO0hO9sY1xA0vp0AZDZD"
FB_VERIFY_TOKEN = "hello"

context_here = {}
past = None
main_intent = None
sess_id = None
sender = None

#bot = Bot(FB_ACCESS_TOKEN)

# Facebook Messenger GET Webhook
@app.route('/', methods=['GET'])
def verify():
    #Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == FB_VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Token verified", 200

# Facebook Messenger POST Webhook
@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            # get all the messages
            for event in entry['messaging']:
                #IDs
                sender_id = event['sender']['id']
                recipient_id = event['recipient']['id']
                if event.get('message'): #and sender_id not in '1025076087628659':
                    if 'text' in event['message']:
                        global sess_id
                        global context_here
                        sess_id = event['timestamp']
                        global past
                        if sess_id == past:
                            return "Old news", 200
                        else:
                            past = sess_id
                            context_here = {}
                        message_text = event['message']['text']
                        context_here = client.run_actions(session_id = sender_id, message = message_text, context = context_here)
                        
                        log("The session state is now:" + str(context_here))
                    else:
                        message_text = None
                    #bot.send_text_message(sender, reply)
                else:
                    print("Not a message")
    else:
        return "Not a page event"
    return "ok", 200

        
def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug = True, port = 80)
