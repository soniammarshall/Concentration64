
from __future__ import print_function
import words
import random

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_dialog_delgate(intent_name, slot_name):
    return { 
        "type": "Dialog.Delegate",
        "updatedIntent": {
            "name": intent_name,
            "slots": {
              slot_name: {
                "name": slot_name
              }
            }
          }
        }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():


    session_attributes = {}
    speech_output = "Welcome to concentration sixty four! Please pick a category"
    reprompt_text = ""
    should_end_session = False
    card_title = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for playing concentration sixty four."
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

    

def check_word(intent, session):
    print(session)
    remaining_words = session.get('attributes', {}).get('remaining words', [])
    category = session.get('attributes', {}).get('category', '')
    
    slots = intent['slots']
    word = slots['word']['value']

    session_attributes = {}
    
    if category == '':
        speech_output = "Choose a category first!"
        should_end_session = False
    elif word is None: 
        speech_output = "You hesitated, game over!"
        should_end_session = True
    elif word not in words.categories[category]:
        speech_output = "That's not in {}, game over!".format(category)
        should_end_session = True
    elif word in remaining_words:
        remaining_words.remove(word)
        if remaining_words:
            alexas_word = alexas_turn(intent, session, remaining_words)
            remaining_words.remove(alexas_word)
            speech_output ="My turn! {} ".format(alexas_word)
        else:
            speech_output = "I've run out of words! You win."
        
        session_attributes = {'remaining words': remaining_words, 'category': category}
        should_end_session = False
    else:
        speech_output ="{} has been said before, you lose".format(word)
        should_end_session = True
        
  
    card_title = ""
    reprompt_text = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))   
        
def choose_category(intent, session):
    slots = intent['slots']
    category = slots['category']['value']
    
    session_attributes = {}
    if category is None:
        speech_output = "I didn't hear you, repeat your category please."
    elif category in words.categories.keys():
        remaining_words = words.categories[category]
        session_attributes = {'remaining words': remaining_words, 'category': category}
        
        speech_output = "The category is {}, let's begin! You start.".format(category)
    else:
        speech_output = "{} is not a valid category. Choose a new one!".format(category)
    
    should_end_session = False 
    
    card_title = ""
    reprompt_text = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))  
        
def alexas_turn(intent, session, remaining_words):
    word = random.choice(remaining_words)
    return word

#Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "wordIntent":
        return check_word(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "chooseCategoryIntent":
        return choose_category(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


def handle_event(event, context):
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def debug(event, context):
    print(event)
    response = handle_event(event, context)
    print(response)
    return response
# --------------- Main handler ------------------

def lambda_handler(event, context):
    # return handle_event(event, context)
    return debug(event, context)
 
