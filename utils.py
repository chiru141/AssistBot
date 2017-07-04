from wit import Wit 
from gnewsclient import gnewsclient

access_token = "6WVGCDAFUAAMGDN5AX2JOPDIK55HJJU4"

client = Wit(access_token = access_token)
message_text="hey there"
def wit_response1(message_text):
	resp = client.message(message_text)
        print resp
	categories = {'newstype':None, 'location':None}

	
	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']
	
	return categories


def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''

	if categories['newstype'] != None:
		news_client.query += categories['newstype'] + ' '

	if categories['location'] != None:
		news_client.query += categories['location']

	news_items = news_client.get_news()

	elements = []

	for item in news_items:
		element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "Read more",
								'url': item['link']
					}],
					'image_url': item['img']		
		}
		elements.append(element)

	return elements