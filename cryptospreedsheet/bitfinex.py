import requests
from time import sleep
import json


class Bitfinex(object):
    BASE_URL = 'https://api.bitfinex.com/v1'

    def get_symbols(self):
        end_point = '/symbols'
        url = self.BASE_URL + end_point
        data = json.loads(requests.get(url).text)
        return data

    def get_ticker(self, symbol):
        end_point = '/pubticker/{}'.format(symbol)
        url = self.BASE_URL + end_point
        data = json.loads(requests.get(url).text)
        return {'ask': data['ask'], 'bid': data['bid'], 'currency': symbol}

    def get_tickers(self):
        d = []
        symbols = self.get_symbols()
        for symbol in symbols:
            d.append(self.get_ticker(symbol))
            sleep(3)
        return d

# btf = Bitfinex()
# btf.get_tickers()
