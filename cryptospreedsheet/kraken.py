import requests
from time import sleep
import json


class Kraken(object):
    BASE_URL = 'https://api.kraken.com/0/public'

    def get_symbols(self):
        end_point = '/AssetPairs'
        url = self.BASE_URL + end_point
        data = json.loads(requests.get(url).text)
        return data['result'].keys()

    def get_ticker(self, symbol):
        end_point = '/Ticker?pair={}'.format(symbol)
        url = self.BASE_URL + end_point
        ticker = ''
        try:
            ticker = requests.get(url).text
            data = json.loads(ticker)['result'][symbol]
            content = {'ask': data['a'][0], 'bid': data['b'][0], 'currency': symbol}
        except Exception as e:
            content = {'ask': e, 'bid': ticker, 'currency': symbol}
        return content

    def get_tickers(self):
        d = []
        symbols = self.get_symbols()
        for symbol in symbols:
            d.append(self.get_ticker(symbol))
            # sleep(3)
        return d

# kkn = Kraken()
# symbols = kkn.get_symbols()
# for symbol in symbols:
#     print(kkn.get_ticker(symbol))
# print(kkn.get_tickers())