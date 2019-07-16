import time

import redis



class Redis:
    def __init__(self):
        try:
            self.conn = redis.Redis(host='redis', port=6379, db='dumb_model')
        except:
            time.sleep(1)
            self.__init__()

    def get(self, key):
        return self.conn.get(key)
