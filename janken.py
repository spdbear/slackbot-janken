import json
import random
from urllib.parse import parse_qs

def janken_result(you, bot):
    result = (you - bot + 3) % 3
    message = [
    ":u7121::u7121:  *DRAW*  :u7121::u7121:",
    ":fire::fire: *YOU LOSE* :fire::fire:",
    ":tada::tada: *YOU WIN* :tada::tada:"]
    return message[result]
    

def lambda_handler(event, context):
    body = parse_qs(event["body"])
    hands = [":fist:", ":v:", ":hand:"]
    your_hand = "" 
    if("text" in body):
        your_hand = body["text"][0]
    if your_hand not in hands:
        your_hand = random.randint(0,2)
    else:
        your_hand = hands.index(your_hand)
        
    bot_hand = random.randint(0,2)
    text = f"""
じゃんけんぽん！
YOU : {hands[your_hand]} :zap: {hands[bot_hand]} : BOT
{janken_result(your_hand, bot_hand)}
    """
    
    return {
        'statusCode': 200,
        'body': text
    }
