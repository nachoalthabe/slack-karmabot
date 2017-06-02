handlers = ['message']

def process(path, data):
    response = False
    if data['event']['type'] in handlers:
        module = __import__(path+data['event']['type'],globals(),locals(),['process'])
        response = module.process(path + data['event']['type'] + '.', data)
    return response