handlers = ['event_callback', 'url_verification']

def process(path,data):
    response = False
    print()
    if data['type'] in handlers:
        module = __import__(__package__+'.'+data['type'],globals(),locals(),['process'])
        response = module.process(path + data['type'] + '.',data)
    return response