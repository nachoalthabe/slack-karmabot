"""Que puede procesar?"""
HANDLERS = ['event_callback', 'url_verification']

def get_flag(data):
    """Que atributo lo define?"""
    return data['type']


def process(path, data):
    """Resuelve si puede procesar, de ser asi procesa"""
    response = ""
    flag = get_flag(data)
    if flag in HANDLERS:
        module = __import__(
            path + flag, globals(), locals(), ['process'])
        response = module.process(path + flag + '.', data)
    return response
