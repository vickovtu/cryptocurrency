import time
import requests


# Получить последнюю цену с Эксмо
def get_exmo_rates(stock_rates):
    while True:
        try:
            api = "https://api.exmo.com/v1/ticker/"
            stock_rates['exmo'] = requests.get(api).json()['ETH_BTC']['last_trade']
        except Exception as e:
            print(e)
        time.sleep(0.5)


# Получить последнюю цену с Binance
def get_binance_rates(stock_rates):
    while True:
        try:
            api = "https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC"
            stock_rates['binance'] = requests.get(api).json()['price']

        except Exception as e:
            print(e)
        time.sleep(0.5)


# Получить последнюю цену с Bittrex
def get_bittrex_rates(stock_rates):
    while True:
        try:
            api = "https://bittrex.com/api/v1.1/public/getticker?market=BTC-ETH"
            stock_rates['bittrex'] = str(requests.get(api).json()['result']['Last'])
        except Exception as e:
            print(e)
        time.sleep(0.5)
