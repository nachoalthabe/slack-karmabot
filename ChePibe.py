"""ChePibe"""
"""request.get_json no retorna nada sin esta linea..."""
import json
from flask import Flask, request, abort
from settings import SLACK_VERIFICATION_TOKEN

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hola! soy ChePibe"

import Incoming
@app.route("/slack", methods=['POST'])
def slack():
    params = request.get_json()
    if params['token'] != SLACK_VERIFICATION_TOKEN:
        abort(404)
    return Incoming.process('Incoming.', params)

if __name__ == "__main__":
    app.run(debug=True)
    