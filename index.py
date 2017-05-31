from flask import Flask, request, jsonify
from slackclient import SlackClient
import json
import re

from settings import SLACK_TOKEN


app = Flask(__name__)

# https://regex101.com/r/1xb3kq/1/
karmaRegex = r"<@[A-Z0-9]*>\ *(\+|\-){2,}"
userRegex = r"<@([A-Z0-9]*)>"
karmaMap = {}
sc = SlackClient(SLACK_TOKEN)

# Validacion, te manda un challange y lo tenes que devolver
# +i: https://api.slack.com/events-api#subscriptions
@app.route("/", methods=['POST', 'GET'])
def hello():
    print('KarmaBot!')
    params = request.get_json()
    if params != None:
        print('-',params)
        if params['type'] == "event_callback":
            event = params['event']
            if event['type'] == "message":
                matches = re.finditer(karmaRegex, event['text'])
                for matchNum, match in enumerate(matches):
                    karamRaw = match.string
                    user = re.findall(userRegex, karamRaw).pop()
                    localKarma = karamRaw.count('+') - karamRaw.count('-')
                    karmaMap[user] = karmaMap.get(user,0) + localKarma
        response = jsonify(params)
    else:
        response = jsonify(karmaMap)
    
    return response

if __name__ == "__main__":
    app.run()
    