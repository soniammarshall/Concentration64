
from __future__ import print_function
import words

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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
    speech_output = "Welcome to concentration sixty four!"
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


def sayHello(intent, session):
    
    session_attributes = {}
    should_end_session = False
    slots = intent['slots']
    
    if 'name' not in slots:
        return build_response(session_attributes, build_dialog_delgate('hello', 'name'))
    
    if 'value' not in slots['name']:
        return build_response(session_attributes, build_dialog_delgate('hello', 'name'))
        
    name = slots['name']['value']
    
    speech_output = "Hello {}, I'm cat game".format(name)
    
    card_title = ""
    reprompt_text = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def play_game(intent, session):
    
    session_attributes = {}
    should_end_session = False
    slots = intent['slots']
    
    speech_output = "Hello, I'm cat game"
    
    card_title = ""
    reprompt_text = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))     

def check_word(intent, session):
    print(session)
    used_words = session.get('attributes', {}).get('used_words', [])
    category = 'fruit' # Todo get from session
    
    # TODO check that word has a value
    
    slots = intent['slots']
    word = slots['word']['value']
    
    # TODO check if the word in the category
    
    
    should_end_session = False
    
    if word not in used_words:
        speech_output ="Your word is {}".format(word)
        used_words.append(word)
    else:
        speech_output ="You said {} before, you lose".format(word)
        shouldEndSession = True
    
    session_attributes = {'used_words': used_words}
    
  
    card_title = ""
    reprompt_text = ""
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))     

# --------------- Events ------------------

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

    # Dispatch to your skill's intent handlers
    if intent_name == "hello":
        return sayHello(intent, session)
    elif intent_name == "playIntent":
        return play_game(intent, session)
    elif intent_name == "wordIntent":
        return check_word(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
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
 