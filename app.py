import os,sys
import general_knowledge
from flask import Flask,request
#from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)
PAGE_ACCESS_TOKEN ="EAAJHRsRCiU0BAOX5oN3I6Y1eW4I9DZBObzHhlrJZAHZCnmnLshqlAm0WfrPFX0hUajilBh8K3aprxsus9C2jeudo4ZCVaLsOotDuToTLl5cyue8zKOzvttnZARNGuufb3Sl5vZA6zKgkd659fzZClGGZBfcnBcnFNo5559fjrLHyigZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)
@app.route('/', methods=['GET'])
def verify():
      #Webhook Verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"],200
    return "Hello World",200



@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if(data['object']) == 'page':
       for entry in data['entry']:
         for messaging_event in entry['messaging']:
            sender_id = messaging_event['sender']['id']
            recipient_id = messaging_event['recipient']['id']
       
            if messaging_event.get('message'):
                if 'text' in messaging_event['message']:
                    messaging_text=messaging_event['message']['text']
                else:
                    messaging_text='no text'
            #response = messaging_text
            response = general_knowledge.main(messaging_text)
            bot.send_text_message(sender_id,response)
            

    return "ok",200

    
def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)


       
