from random import shuffle
import sys
from wit import Wit
 

access_token= "MGMGAD7W5MP2CQNPMZWJWY7RVE4VPR3R"
all_jokes = {
    'traditional': [
        'Rajnikanth counted to infinity - twice.',
        'Death once had a near-Rajnikanth experience.',
        'Why was the Math book sad? Because it had so many problems.',
        "Yo momma is so fat, I took a picture of her last Christmas and it's still printing.",
        'Yo momma is so fat when she got on the scale it said, "I need your weight not your phone number."',
        "Yo momma's so fat, that when she fell, no one was laughing but the ground was cracking up.",
        'Yo mamma is so ugly when she tried to join an ugly contest they said, "Sorry, no professionals."',
        'Yo momma is so fat that when she went to the beach a whale swam up and sang, "We are family, even though you\'re fatter than me."',
        'Yo momma is so fat when she sat on WalMart, she lowered the prices.',
        'Teacher: "Kids, what does the chicken give you?"Student: "Meat!"Teacher: "Very good! Now what does the pig give you?"Student: "Bacon!"Teacher: "Great! And what does the fat cow give you?"Student: "Homework!"',
        'Student: "Meat!"Teacher: "Very good! Now what does the pig give you?"Student: "Bacon!"Teacher: "Great! And what does the fat cow give you?"Student: "Homework!"',
        'Yo momma\'s so fat and old when God said, "Let there be light," he asked your mother to move out of the way.',
        "Yo momma is so fat that Dora can't even explore her!",
        'Yo momma is so stupid when an intruder broke   into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldn\'t find the "CALL" button.',
        'Your momma is so ugly she made One Direction go another direction.',
        'Yo momma is so fat her bellybutton gets home 15 minutes before she does.',
        'Q: What is the difference between a cat and a comma?A: One has claws at the end of its paws and the other is a pause at the end of a clause.',
        'Q: Why do hamburgers go to the gym A: To get better buns!',
        "What is a dentist's favorite Dinosaur? A Flossorapter",
        "I just read a book about Helium. It was so good that I can't put it down.",
       'Teacher: What is the value of Pi?Student: Depending on what pie. Usually is $12.99',
       'A teacher asks her class what their favorite letter is. A student puts up his hand and says \'G\'. The teacher walks over to him and says, "Why is that, Angus?"',
       'I have a stepladder. I never knew my real ladder.',
       'Q: Who cares if you pee in the shower?A: The bride and all her guests, apparently.',
        'Five out of six people agree that Russian Roulette is safe.',
       'Q: How does Albus get into Hogwarts?A: Through the Dumble-door.',
            'How is Christmas like your job? You do all the work and the fat guy in the suit gets all the credit.',

    ],
    'technology': [
        'Did you hear about the two antennas that got married? The ceremony was long and boring, but the reception was great!',
        'Why do geeks mistake Halloween and Christmas? Because Oct 31 === Dec 25.',
        'Reaching the end of a job interview, the Human Resources Officer asks a young engineer fresh out of the Massachusetts Institute of Technology, "And what starting salary are you looking for?" The engineer replies, "In the region of $125,000 a year, depending on the benefits package." The interviewer inquires, "Well, what would you say to a package of five weeks vacation, 14 paid holidays, full medical and dental, company matching retirement fund to 50% of salary, and a company car leased every two years, say, a red Corvette?" The engineer sits up straight and says, "Wow! Are you kidding?" The interviewer replies, "Yeah, but you started it."',
        'Q: Why couldn\'t the blonde add 10 + 5 on a calculator? A: She couldn\'t find the "10" button.',
        'Q: What do computers eat for a snack? A: Microchips!',
        'Q: What computer sings the best? A: A Dell.',
        'The energizer bunny was arrested on a charge of battery.',
    ],
    'animal': [
        "What happens to a frog's car when it breaks down?It gets toad away.",
 'It gets toad away.',
 'Q: What did the duck say when he bought lipstick?A: "Put it on my bill."',
 'A: "Put it on my bill."',
 'A boy is selling fish on a corner. To get his customers\' attention, he is yelling, "Dam fish for sale! Get your dam fish here!" A pastor hears this and asks, "Why are you calling them \'dam fish.\'" The boy responds, "Because I caught these fish at the local dam." The pastor buys a couple fish, takes them home to his wife, and asks her to cook the dam fish. The wife responds surprised, "I didn\'t know it was acceptable for a preacher to speak that way." He explains to her why they are dam fish. Later at the dinner table, he asks his son to pass the dam fish. He responds, "That\'s the spirit, Dad! Now pass the f*cking potatoes!"',
 'A blonde and a redhead have a ranch. They have just lost their bull. The women need to buy another, but only have $500. The redhead tells the blonde, "I will go to the market and see if I can find one for under that amount.  If I can, I will send you a telegram."  She goes to the market and finds one for $499. Having only one dollar left, she goes to the telegraph office and finds out that it costs one dollar per word. She is stumped on how to tell the blonde to bring the truck and trailer. Finally, she tells the telegraph operator to send the word "comfortable." Skeptical, the operator asks, "How will she know to come with the trailer from just that word?" The redhead replies, "She\'s a blonde so she reads slow: \'Come for ta bull.\'"',
 "Q: Can a kangaroo jump higher than the Empire State Building? A: Of course. The Empire State Building can't jump.",

 'Q: How do you count cows? A: With a cowculator.',
 "Q: Why did the witches' team lose the baseball game? A: Their bats flew away.",
 'There was a papa mole, a momma mole, and a baby mole. They lived in a hole out in the country near a farmhouse. Papa mole poked his head out of the hole and said, "Mmmm, I smell sausage!" Momma mole poked her head outside the hole and said, "Mmmm, I smell pancakes!" Baby mole tried to stick his head outside but couldn\'t because of the two bigger moles. Baby mole said, "The only thing I smell is molasses."',
 'Two bats are hanging upside down on a branch. One asks the other, "Do you recall your worst day last year?" The other responds, "Yes, the day I had diarrhea!"',
        ],
}
def wit_response(sender_id, messaging_text):
    client.run_actions(session_id=sender_id, message=messaging_text)
    #print request['entities']
    #print type(request)
    #request.update({'context':{}})
    #print request

def first_entity_value(entities, entity):
    if entity not in entities:
       return None
    
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def second_entity_value(entities, entity):
    if entity not in entities:
       return None
    
    val = entities[entity][1]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    global fb_response
    fb_response=response['text']
    #print(response['text'])

def response_fb():
    return fb_response
        
def merge(request):
    context = request['context']
    print context
    entities = request['entities']
    print entities

    if 'joke' in context:
        del context['joke']
    greet = first_entity_value(entities, 'greet')
    if greet:
        context['greet'] = 'Greetings'
    
    emotion = first_entity_value(entities, 'emotion')
    if emotion:
        context['emot'] = 'I can cheer you up. ' if emotion == 'sad' else ' I am so happy for you.' 
    intent = first_entity_value(entities, 'intent')
    if intent:
        context['intro']=' I tell jokes. If you are upset or bored, I can cheer you up with my funny jokes'
    jokenum = first_entity_value(entities, 'jokenum')
    if jokenum:
        context['num']=jokenum
    joketype1 = first_entity_value(entities, 'joketype')
    if joketype1:
       if  len(entities['joketype']) > 1:
          joketype2 = second_entity_value(entities, 'joketype')
          if joketype1  and  joketype2:
             context['cat'] = joketype2
       elif  len(entities['joketype']) == 1:
          context['cat'] = joketype1
    yesno = first_entity_value(entities, 'yesno')
    if yesno:
        context['ny']= 'I will try my best to make you laugh' if yesno== 'yes' else 'Okay, see you later.'
    bubye = first_entity_value(entities, 'bubye')
    if bubye:
        context['bubye'] = 'Goodbye. Take care'
    sentiment = first_entity_value(entities, 'sentiment')    
    if sentiment:
        context['ack'] = 'Ohh!I am so good at my job!.' if sentiment == 'positive' else 'Hmm. I think I need to work more on my humour. '
    elif 'ack' in context:
        del context['ack']
    return context

def select_joke(request):
    #shuffle(jokes)
       context = request['context']
       jokes = all_jokes[context['cat'] or 'traditional']
       shuffle(jokes)
       context['joke'] = jokes[0]
       return context
    
def select_joke1(request):
    #shuffle(jokes)
       context = request['context']
       jokes = all_jokes[context['cat'] or 'traditional']
       shuffle(jokes)
       context['joke1'] = jokes[1]
       return context


actions = {
    'wit-response':wit_response,
    'send': send,
    'merge': merge,
    'select-joke': select_joke,
    'select-joke1':select_joke1,
    
}
client = Wit(access_token=access_token, actions=actions)
#client.interactive()

