from wit import Wit

access_token = "GPOOEJ2VHEGD5BA5C5EFZ3GZ4YYFTBZ2"





def wit_response(message_text):
	resp = client.message(message_text)
	entity = None
	value = None 
	
	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass	
	return(entity, value)
	

	client.run_actions(session_id, message_text)	

	actions = {
		'send':send,
		'merge':merge,
   # 'my_action':my_action,
}

	client = Wit(access_token = access_token, actions=actions)

	client.interactive()	
#def wit_converse()
		
	
#print(wit_response("i want chinese"))

#  message_text = "i am his sister"
 