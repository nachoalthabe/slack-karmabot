# Procesa un mensaje en busca de karmas, si existe lo procesa y actualiza
# los datos

import re
from slackclient import SlackClient
from settings import SLACK_TOKEN
sc = SlackClient(SLACK_TOKEN)

# https://regex101.com/r/1xb3kq/1/
karmaRegex = r"<@[A-Z0-9]*>\ *(\+|\-){2,}"
userRegex = r"<@([A-Z0-9]*)>"
karmaMap = {}


def process(data):
    matches = re.finditer(karmaRegex, data['event']['text'])
    touchedUsers = []
    for matchNum, match in enumerate(matches):
        karamRaw = match.string
        user = re.findall(userRegex, karamRaw).pop()
        localKarma = karamRaw.count('+') - karamRaw.count('-')
        karmaMap[user] = karmaMap.get(user, 0) + localKarma
        touchedUsers.append(user)
        response(data,user,localKarma,karmaMap[user])
    return "KarmaBot!"

def response(data, user, localKarma, value):
    if (localKarma > 0):
        direction = 'aumento'
    else:
        direction = 'disminuyo'
    sc.api_call(
        "chat.postMessage",
        channel=data['event']['channel'],
        text='<@{0}> {1} su karma a {2}'.format(user, direction, value)
    )
