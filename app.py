import os, sys
from flask import Flask, request
from joke import response_fb,wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAEYD3T8JdIBANGspd0jifk3klujUZAZCeJtUIoHeexttjyLDFZBGJXnRaZCQCRog0Fy5X0nHjrxT9mQJyXN2sQVoewT0yE78U5KMCZCmCnZCYQmVjoQrdZCwaC3kVdmAAdALEplzPmhtZBqzsfEhVKbjx8mIGRgOqjZBdBSvK3q447PDwbgtkxDc"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Verification for webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# Retrieval of IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'
                                        
					wit_response(sender_id,messaging_text) #send message to wit.ai engine
					response = response_fb()
					print response
					bot.send_text_message(sender_id, response) #send response to fb
					
	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
