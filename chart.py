import string

import matplotlib.pyplot as plt

import stock_api


def create_chart(stock_id: string):
    stock_data = stock_api.Stock_API(stock_id).get_history_price(2020, 1)
    dates, prices = data_format(stock_data)
    plt.title('price')
    plt.gcf().autofmt_xdate()
    plt.plot(dates, prices)
    plt.show()
    plt.savefig('plot.png')
    return ''


def data_format(stock_data):
    dates = []
    prices = []
    for data in stock_data:
        dates.append(data[0].strftime('%y/%m/%d'))
        prices.append(data[6])
    return dates, prices
