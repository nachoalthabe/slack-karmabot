from Incoming.event_callback.message import karma

def process(path, data):
    response = ""
    response += karma.process(data)
    return response