# -*- coding: utf-8 -*-
import os, sys
from flask import Flask, request
import general_knowledge
from utils import wit_response1, get_news_elements
from utils_main import wit_response_main
from joke import response_fb,wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAEYD3T8JdIBAL1LlnX3I1NZCNf68mYLI0s30bO3H9BYsyZALNn3obDUK0YSfIoY6nzwFwpZCcZBoDWZCoZBSFYJ0nDZARd3CPuXtyzW7yOlj7PKp81x8CGV5cO4pXoZAQACuivh2Sj5ya52MUsOzBKLfop0N9Y4kBXvBqboQFshV5ZCjfZCwdozNc"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
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

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'
					categories = wit_response_main(messaging_text)
					if(categories['NewsBot']!= None):
						categories1 = wit_response1(messaging_text)
						elements = get_news_elements(categories1)
						bot.send_generic_message(sender_id, elements)

					elif(categories['JokeBot']!= None):
                                                wit_response(sender_id,messaging_text)
					        response = response_fb()
					        bot.send_text_message(sender_id,response)

					elif(categories['FoodBot']!= None):
                                                wit_response_food(sender_id,messaging_text)
					        response = response_fb()
					        bot.send_text_message(sender_id,response)
					        
				        """else:
                                            reponse_none= "Sorry, I could not get what you said. I am a baby bot and I am still in my learning period"
                                            bot.send_text_message(sender_id,response_none)      """
					

					   
					"""elif(categories['gkBot']!= None):
						response_gk = general_knowledge.main(messaging_text)
						bot.send_text_message(sender_id,response_gk)"""

					
	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
