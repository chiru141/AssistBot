from wit import Wit 

access_token = "7EIAZJHENGJXAXIQXPYXOPYWOX7HMPAU"

client = Wit(access_token = access_token)

def wit_response_main(message_text):
	resp = client.message(message_text)
	categories = {'NewsBot': None, 'gkBot': None, 'FoodBot': None, 'JokeBot': None}
	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']
	
	return categories