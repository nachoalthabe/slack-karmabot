import { SLACK_TOKEN } from './settings'

const WebClient = require('@slack/client').WebClient;

var web = new WebClient(SLACK_TOKEN);

function sendMessage(message, channel) {
    web.chat.postMessage(channel, message, function (err, res) {
        if (err) {
            console.error('SlackClient.sendMessage:', err);
        }
    });
}

export { sendMessage }