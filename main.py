import re
import long_responses as long

def msg_prob(user_msg, recognised_words, single_response=False, required_words=[]):
    msg_certainity = 0
    has_required_words = True

    for word in user_msg:
        if word in recognised_words:
            msg_certainity += 1

    percentage = float(msg_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_msg:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_msg(msg):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_prob(msg, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])


    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])


    best_match = max(highest_prob_list, key = highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match]< 1 else best_match

def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_msg(split_msg)
    return response

while True:
    print('Bot:' + get_response(input('You: ')))
