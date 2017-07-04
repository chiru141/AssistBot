from wit import Wit
import requests
import os, sys
from random import shuffle
from pprint import pprint

WIT_ACCESS_TOKEN = "JZX4W3L7JFPQQMPCNUFBXVELGH7JGDG5"
zomato_api_key="bdb3b7c195a74c2b0deefe4534c6a410"
URL_zomatoApi_param = "?apikey=bdb3b7c195a74c2b0deefe4534c6a410"
BasicURL = "https://developers.zomato.com/api/v2.1/"

count = 0
main_intent = None

def fb_message(sender_id, text):
    """
    Function for returning response to messenger
    """
    data = {
        'recipient': {'id': sender_id},
        'message': {'text': text}
    }
    # Setup the query string with your PAGE TOKEN
    qs = 'access_token=' + FB_ACCESS_TOKEN
    # Send POST request to messenger
    resp = requests.post('https://graph.facebook.com/me/messages?' + qs,
                         json=data)
    return resp.content


def first_entity_value(entities, entity):
    #Return first entity value
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def send(request, response):
    #Sender function
    sender_id = request['session_id']
    text = response['text']
    # send message
    fb_message(sender_id,text.decode('utf-8'))

#def send(request, response):
#	text = response['text']
#	print text

def get_SignOffGreeting(request):
	context=request['context']
	signOffgreetings = ["bye", "See you", "Enjoy!", "Good day", "take care", "have a nice day :)"]
	shuffle(signOffgreetings)
	#pprint(request)
	context['signOffGreeted'] = 'true'
	context['signOffGreetWith'] = signOffgreetings[0]
	#pprint(context)
	return context
	
def get_HungerReplies(request):
	context=request['context']
	if context.get('greeted') is not None:
		del context['greeted']
	hungerReplies = ["Go out and eat!", "let me suggest you a good place", "great, let's get food", "Aww, let's find a place for you to eat", "chill, i will help you find a place"]
	shuffle(hungerReplies)
	pprint(request)
	context['hungerReplied'] = 'true'
	context['hungerReply'] = hungerReplies[0]
	#pprint(context)
	return context
	
	
def get_greeting(request):
	context=request['context']
	greetings = ["Hey", "Hi", "Hello", "Hi, what's up?", "How you doin?", "hey there"]
	shuffle(greetings)
	#pprint(request)
	context['greeted'] = 'true'
	context['greetWith'] = greetings[0]
	#pprint(context)
	return context

def get_restaurant(request):
	global count
	log("1111111 In Restaurant 222222") 
	pprint(request) 
	context = request['context']
	entities = request['entities']
	pprint(context)
    #log(entities)
	if context.get('greeted') is not None:
		del context['greeted']
	if context.get('hungerReplied') is not None:
		del context['hungerReplied']
	if context.get('result') is not None:
		del context['result']
		count += 1
		context['count']=count
	if context.get('missingLocation') is not None:
		del context['missingLocation']
	if context.get('missingCuisine') is not None:
		del context['missingCuisine']
	if context.get('errorEvent') is not None:
		del context['errorEvent']
			
	location = first_entity_value(entities, 'location')
	if location:
		setLocation(context, location)
	elif 'setLocation' in context:
		pprint(context)
	else:
		context['missingLocation'] = True
		
	if context.get('location') is not None:
		cuisine = first_entity_value(entities, 'cuisine')
		if cuisine:
			setCuisine(context, cuisine)
			
		elif 'setCuisine' in context:
			setCuisine(context, context['cuisine_name'])
			pprint(context)
			
		else:
			context['missingCuisine'] = True
	
	
	if context.get('missingLocation') is not None:
		cuisine = first_entity_value(entities, 'cuisine')
		if cuisine:
			context['setCuisine']='true'
			context['cuisine_name']=first_entity_value(entities, 'cuisine')
			
	if context.get('missingLocation') is None and context.get('missingCuisine') is None: 
		data=findRestaurant(context)
		    
		if context.get('errorEvent') is not None:
			log(context['errorEvent'])
			log(context)
			return context
            
		if data['results_found'] == 0:
			context['errorEvent'] = "No results found"
			log("No results found in ",location)
			log(context)
			return context
		else:
			context['result'] = data['restaurants'][count]['restaurant']['name'] + " Address: "  + data['restaurants'][count]['restaurant']['location']['address']
            #if
			say = ["Why don't you try", "You could visit", "Drop by", "Try out", "I recommend", "How about"]
			shuffle(say)
			context['say'] = say[0]
		

	print "before out of get_restaurant"
	pprint(context)
	return context

def setLocation(context, location):
	URL_location = BasicURL + "locations?apikey=" + zomato_api_key 
	URL_location = URL_location + "&query=" + location
	response = requests.get(URL_location)
	data=response.json()

	if data['status'] != 'success':
		context['errorEvent'] = 'true'
		return context
	else:
		context['location'] = location
		context['city_id']= data['location_suggestions'][0]['city_id']
		context['location_lat']=data['location_suggestions'][0]['latitude']
		context['location_long']=data['location_suggestions'][0]['longitude']
		context['setLocation'] = 'true'
	return context
	
def setCuisine(context, cuisine):
	URL_availCuisines = BasicURL + "cuisines" + URL_zomatoApi_param
	
	URL_availCuisines=URL_availCuisines	+ "&city_id="+str(context['city_id'])
	
	response = requests.get(URL_availCuisines)
	data=response.json()
	length=len(data['cuisines'])
	
	flag=0
	for i in range(0,length):
		if data['cuisines'][i]['cuisine']['cuisine_name'].lower() == cuisine.lower():
			context['cuisine_name']=cuisine
			context['cuisine_id']=data['cuisines'][i]['cuisine']['cuisine_id']
			context['setCuisine']='true'
			flag = 1
			break
	
	if flag != 1:
		context['errorEvent'] = 'true'
		fb_response= "cuisine doesn't exist in the location"
		
	return context

def findRestaurant(context): 
		URL_findRestaurant = BasicURL + "search" + "?apikey=" + zomato_api_key + "&sort=rating&order=desc"
		print "in find Restaurant- request"
		pprint(context)
		
		if 'cuisine_id' in context:
			print "search wrt cuisine_id"
			URL_findRestaurant = URL_findRestaurant + "&cuisines=" + str(context['cuisine_id'])
		if 'city_id' in context:
			print "search wrt city"
			URL_findRestaurant = URL_findRestaurant + "&entity_id=" + str(context['city_id'])
		if 'location_lat' in context:
			URL_findRestaurant = URL_findRestaurant + "&lat=" + str(context['location_lat'])
		
		if 'location_long' in context:
			URL_findRestaurant = URL_findRestaurant + "&lon=" + str(context['location_long'])
		if 'establishment_id' in context:
			URL_findRestaurant = URL_findRestaurant + "&establishment_type=" + str(context['establishment_id'])
		if 'category_id' in context:
			URL_findRestaurant = URL_findRestaurant + "&category=" + str(context['category_id'])

		response = requests.get(URL_findRestaurant)
		#print response
		data=response.json()
		return data
			
# Setup Actions

actions = {
    'send': send,
    'getRestaurant': get_restaurant,
	'getGreetings':get_greeting,
	'getSignOffGreeting':get_SignOffGreeting,
	'getHungerReplies':get_HungerReplies
}

def log(message):
    print(message)
    sys.stdout.flush()

client = Wit(access_token = WIT_ACCESS_TOKEN, actions = actions)

#client.interactive()

