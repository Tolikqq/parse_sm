import os
from datetime import datetime
import http.cookiejar as cookielib
import urllib.request as unlib

import requests

class Smotreshka:

    NEWS_CATEGORY_ID = 1
    MOVIES_CATEGORY_ID = 2
    SPORT_CATEGORY_ID = 3
    AIR_CATEGORY_ID = 4
    FAVORITES_CATEGORY_ID = 5
    ALL_CHANNELS_CATEGORY_ID = 6
    ENTERTAINMENT_CATEGORY_ID = 7
    SCIENCE_CATEGORY_ID=8


    def __init__(self, email, password, dataDir):
        self._email = email
        self._password = password
        self._dataDir = dataDir
        self._cookies = None
        self._userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
        self._categoriesMap = {u'новости':Smotreshka.NEWS_CATEGORY_ID,
                               u'Новости':Smotreshka.NEWS_CATEGORY_ID,
                               u'кино':Smotreshka.MOVIES_CATEGORY_ID,
                               u'Кино':Smotreshka.MOVIES_CATEGORY_ID,
                               u'спорт':Smotreshka.SPORT_CATEGORY_ID,
                               u'Развлекательные':Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'Развлекательный':Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'развлечения':Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'познавательные':Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Познавательные':Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Познавательный':Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Спорт':Smotreshka.SPORT_CATEGORY_ID,
                               u'Эфирные':Smotreshka.AIR_CATEGORY_ID,
                               u'Эфирный':Smotreshka.AIR_CATEGORY_ID,
                               u'основные':Smotreshka.AIR_CATEGORY_ID}
        self._channels_cache = None
        self._channels_last_update = None

    def check(self):

        try:
            return self._login()
        except:
            return False

    def _login(self):
        url = 'http://fe.smotreshka.tv/login'
        values = {'email': self._email, 'password': self._password}
        r = requests.post(url, values)
        if r.status_code == 200:
            return True