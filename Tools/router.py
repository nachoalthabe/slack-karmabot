
def ChePibeRoute(package, handlers):
    def decorator(_function):
        def process(path,data):
            response = False
            if data['type'] in handlers:
                module = __import__(package+'.'+data['type'],globals(),locals(),['process'])
                response = module.process(path + data['type'] + '.',data)
            return response

    
    