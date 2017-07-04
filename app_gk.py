import os,sys
import general_knowledge
from flask import Flask,request
from pymessenger import Bot

app = Flask(__name__)
PAGE_ACCESS_TOKEN ="EAAaNKrpp5cUBACOz4ErWJO2H4iIva3PsyMfQmxNrT5O4Xb2raX6F45ZCuxM4O7a6un2RdUmksT2C9qFeAXkjX2ZCovWt6ZCPZBj7AgU65cvFPw9seUmYPmg5Wc74rkcZChF8XrGtdMVV5FzOT22oOlsoIfXUCAwENHfgKwLNZBF81JCuajvxQH"

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
                    messaging_text = messaging_event['message']['text']
                else:
                    messaging_text = 'no text'
            #response = messaging_text
            response = general_knowledge.main(messaging_text)
            bot.send_text_message(sender_id,response)
            

    return "ok",200

    
def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)


       
