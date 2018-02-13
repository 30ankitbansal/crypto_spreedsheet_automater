import requests
from time import sleep
import json


class Gdax(object):
    BASE_URL = 'https://api.gdax.com/'

    def get_symbols(self):
        end_point = 'products'
        url = self.BASE_URL + end_point
        data = json.loads(requests.get(url).text)
        symbols = []
        for content in data:
            symbols.append(content['id'])
        return symbols

    def get_ticker(self, symbol):
        end_point = 'products/' + symbol + '/ticker'
        url = self.BASE_URL + end_point
        data = json.loads(requests.get(url).text)
        return {'ask': data['ask'], 'bid': data['bid'], 'currency': symbol}

    def get_tickers(self):
        d = []
        symbols = self.get_symbols()
        for symbol in symbols:
            d.append(self.get_ticker(symbol))
            # sleep(3)
        return d

# gdax = Gdax()
# print(gdax.get_symbols())
# print(gdax.get_tickers())