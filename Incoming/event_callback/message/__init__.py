from Incoming.event_callback.message import karma

def process(path, data):
    karma.process(data)
    return True