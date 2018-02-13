import requests
from time import sleep
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from bitfinex import Bitfinex
from kraken import Kraken
from gdax import Gdax
import settings


def update_sheet(gc, filename, obj):
    sheet = gc.open(filename).sheet1
    symbols = obj.get_symbols()
    row = 1
    sheet.update_acell('A' + str(row), 'currency')
    sheet.update_acell('B' + str(row), 'ask')
    sheet.update_acell('C' + str(row), 'bid')
    for symbol in symbols:
        ticker = obj.get_ticker(symbol)
        row += 1
        sheet.update_acell('A' + str(row), ticker['currency'])
        sheet.update_acell('B' + str(row), ticker['ask'])
        sheet.update_acell('C' + str(row), ticker['bid'])
    return str(row) + ' updated in ' + filename


def authorize(credentials_file = settings.CREDENTIALS_FILE):
    json_key = json.load(open(credentials_file))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)
    return gc


def main():
    btf = Bitfinex()
    kkn = Kraken()
    gdax = Gdax()

    gc = authorize()
    print(update_sheet(gc, 'bitfinex', btf))
    print(update_sheet(gc, 'kraken', kkn))
    print(update_sheet(gc, 'gdax', gdax))


main()