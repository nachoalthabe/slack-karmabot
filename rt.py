from init import sc
import time

if sc.rtm_connect():
    while True:
        data = sc.rtm_read()
        if len(data > 0):
            print('RT: ', data)
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")