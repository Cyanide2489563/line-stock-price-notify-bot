import string
import time

import twstock

twstock.__update_codes()


def is_stock(stock_code: string):
    return stock_code in twstock.codes


class Stock_API:

    def __init__(self, stock_code: string):
        self.stock_code = stock_code

    def get_stock(self):
        time.sleep(2)  # 防止 IP 遭到證交所 Ban 掉
        stock_data = twstock.realtime.get(self.stock_code)
        return Stock_Data(stock_data)

    def get_history_price(self, year: int, month: int):
        time.sleep(2)  # 防止 IP 遭到證交所 Ban 掉
        stock_data = twstock.Stock(self.stock_code)
        return stock_data.fetch_from(year, month)


class Stock_Data:

    def __init__(self, stock_data: dict):
        self.stock_data = stock_data

    def name(self):
        return self.stock_data['info']['name']

    def time(self):
        return self.stock_data['info']['time']

    def price(self):
        return self.stock_data['realtime']['latest_trade_price']

    def open_price(self):
        return self.stock_data['realtime']['open']

    def high_price(self):
        return self.stock_data['realtime']['high']

    def low_price(self):
        return self.stock_data['realtime']['low']
