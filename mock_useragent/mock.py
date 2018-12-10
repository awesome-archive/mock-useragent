import random
from os import path, makedirs
import json
import os, io
# import mock_useragent.offline_datas.chrome as chromes


# files = os.path.join('./mock_useragent/offline_datas/chrome.json')


def read(path):
    with io.open(path, encoding='utf-8', mode='rt') as fp:
        return json.loads(fp.read())

class MockUserAgent(object):
    ua_list = []
    def __init__(self):
        from mock_useragent.offline_datas.chrome import chromes
        self.ua_list = chromes
        # self.ua_list = read(files)
    

    def chrome(self):
        pass

    def safari(self):
        pass

    def firefox(self):
        pass

    def android(self):
        pass
    @property
    def random_chrome(self):
        # print(self.ua_list)
        return random.choice(self.ua_list)['ua'].replace('\\','')




# t = MockUserAgent() 
# print(t)
# print(t.random_chrome())


UserAgent = MockUserAgent
