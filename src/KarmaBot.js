import { sendMessage } from './SlackClient'

const karmaRegex = /<@[A-Z0-9]*>\ *(\+{2,}|\-{2,})( |$|\n)/g
const userRegex = /<@([A-Z0-9]*)>/g
const currentState = {}

class KarmaBot {

    _process({ userId, localKarma, slackEvent }) {
        let increase = (localKarma > 0)
        if (userId == slackEvent.event.user) {
            if (increase === false){
                return `<@${slackEvent.event.user}> arriba el animo! :hugging_face:`
            }else{
                return `<@${slackEvent.event.user}> :troll:`
            }
        } else if (localKarma > 6) {
            return `<@${slackEvent.event.user}> no se pueden sumar más de 6 puntos :shipit:`
        } else if (localKarma < -6) {
            return `<@${slackEvent.event.user}> no se pueden restar más de 6 puntos :shipit:`
        } else {
            let karma = currentState[userId] = (currentState[userId] || 0) + localKarma
            return `<@${userId}> ${increase ? 'incremento' : 'decremento'} su karma a ${karma}.`
        }
    }

    process(slackEvent) {
        if (slackEvent.type != "event_callback" || slackEvent.event.type != "message")
            return false
        const message = slackEvent.event.text
        var m, matchs = [], touched = []
        while ((m = karmaRegex.exec(message)) !== null) {
            // This is necessary to avoid infinite loops with zero-width matches
            if (m.index === karmaRegex.lastIndex) {
                karmaRegex.lastIndex++;
            }
            // The result can be accessed through the `m`-variable.
            m.forEach((match, groupIndex) => {
                if (groupIndex === 0)
                    matchs.push(match)
            });
        }
        matchs.forEach(match => {
            const userId = match.split(userRegex)[1]
            let localKarma = match.match(/\+/g) || false
            if (localKarma !== false) {
                localKarma = localKarma.length - 1
            } else {
                localKarma = match.match(/\-/g) || false
                if (localKarma !== false) {
                    localKarma = localKarma.length * -1 + 1
                }
            }
            if (localKarma === false) return
            touched.push({ userId, localKarma, slackEvent })
        })
        if (touched.length > 0) {
            sendMessage(touched.map(this._process).join(`\n`), slackEvent.event.channel)
            return true
        }
        return false
    }
}

export default KarmaBot