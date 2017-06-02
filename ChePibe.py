from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
   return "Hola! soy el chepibe"

import Incoming
@app.route("/slack", methods=['POST'])
def slack():
    if Incoming.process('Incoming.', request.get_json()):
        return "Ok"
    else:
        return "Nop"

if __name__ == "__main__":
    app.run(debug=True)
    