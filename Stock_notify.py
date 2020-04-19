import time

import twstock

while True:
    realdata = twstock.realtime.get('2330')
    if realdata['success']:
        price = realdata['realtime']['latest_trade_price']
        # if float(price) >= 100:

