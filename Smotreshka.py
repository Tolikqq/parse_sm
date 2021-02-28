
import requests

proxy_list = 'proxy-list.txt'

class Smotreshka:
    NEWS_CATEGORY_ID = 1
    MOVIES_CATEGORY_ID = 2
    SPORT_CATEGORY_ID = 3
    AIR_CATEGORY_ID = 4
    FAVORITES_CATEGORY_ID = 5
    ALL_CHANNELS_CATEGORY_ID = 6
    ENTERTAINMENT_CATEGORY_ID = 7
    SCIENCE_CATEGORY_ID = 8

    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._cookies = None
        self._proxies = []
        self._userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
        self._categoriesMap = {u'новости': Smotreshka.NEWS_CATEGORY_ID,
                               u'Новости': Smotreshka.NEWS_CATEGORY_ID,
                               u'кино': Smotreshka.MOVIES_CATEGORY_ID,
                               u'Кино': Smotreshka.MOVIES_CATEGORY_ID,
                               u'спорт': Smotreshka.SPORT_CATEGORY_ID,
                               u'Развлекательные': Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'Развлекательный': Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'развлечения': Smotreshka.ENTERTAINMENT_CATEGORY_ID,
                               u'познавательные': Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Познавательные': Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Познавательный': Smotreshka.SCIENCE_CATEGORY_ID,
                               u'Спорт': Smotreshka.SPORT_CATEGORY_ID,
                               u'Эфирные': Smotreshka.AIR_CATEGORY_ID,
                               u'Эфирный': Smotreshka.AIR_CATEGORY_ID,
                               u'основные': Smotreshka.AIR_CATEGORY_ID}
        self._channels_cache = None
        self._channels_last_update = None

    def get_proxies(self):

        with open(proxy_list, 'rt', encoding='utf-8') as proxies_file:

            for line in proxies_file:
                if not line:
                    continue

                ip, port = line.replace('\r', '').split(':')

                port = int(port)
                proxy = {'ip': ip, 'port': port}
                self._proxies.append(proxy)

        return self._proxies

    def check(self):

        try:
            return self._login()
        except:
            return False


    def _login(self):
        url = 'http://fe.smotreshka.tv/login'
        values = {'email': self._email, 'password': self._password}
        r = requests.post(url, values,  timeout=10, allow_redirects=False,
                          verify=False, proxies=self._proxies)

        return r.status_code == 200
