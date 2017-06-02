"""Que puede procesar?"""
from flask import abort
HANDLERS = ['message']

processed = []

def get_flag(data):
    """Que atributo lo define?"""
    return data['event']['type']

def process(path, data):
    """Resuelve si puede procesar, de ser asi procesa"""
    ts = data['event']['ts']
    if ts in processed:
        abort(200)
    processed.append(ts)
    response = ""
    flag = get_flag(data)
    if flag in HANDLERS:
        module = __import__(
            path + flag, globals(), locals(), ['process'])
        response = module.process(path + flag + '.', data)
    return response
