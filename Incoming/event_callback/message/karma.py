# Procesa un mensaje en busca de karmas, si existe lo procesa y actualiza
# los datos

import re

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
        touchedUsers.append(karmaMap[user])
    print(touchedUsers.__len__())

def response(userData):{
    #mandar un mensage con el estado actualizado de los karmas procesados
}
