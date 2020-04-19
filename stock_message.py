import string

from linebot.models import MessageAction, QuickReplyButton, QuickReply, TextSendMessage

import stock_api


def get_stock_info(stock_id: string):
    stock_data = stock_api.Stock_API(stock_id).get_stock()
    info = (
        f'股票名稱：{stock_data.name()}\n'
        f'資料抓取時間：{stock_data.time()}\n'
        f'目前價格：{stock_data.price()}\n'
        f'開盤價格：{stock_data.open_price()}\n'
        f'價格最高：{stock_data.high_price()}\n'
        f'價格最低：{stock_data.low_price()}'
    )
    text_message = TextSendMessage(text=info,
                                   quick_reply=QuickReply(
                                       items=[
                                           QuickReplyButton(
                                               action=
                                               MessageAction(
                                                   label="加入至我的股票",
                                                   text=f'{stock_id}:加入我的股票'
                                               )
                                           ),
                                           QuickReplyButton(
                                               action=
                                               MessageAction(
                                                   label="查看圖表",
                                                   text=f'{stock_id}:查看圖表'
                                               )
                                           )
                                       ]
                                   ))
    return text_message


def get_stock_chart(stock_id: string):

    text_message = TextSendMessage(text='',
                                   quick_reply=QuickReply(
                                       items=[
                                           QuickReplyButton(
                                               action=
                                               MessageAction(
                                                   label="加入至我的股票",
                                                   text=f'{stock_id}:加入我的股票'
                                               )
                                           ),
                                           QuickReplyButton(
                                               action=
                                               MessageAction(
                                                   label="查看圖表",
                                                   text=f'{stock_id}:查看圖表'
                                               )
                                           )
                                       ]
                                   ))
    return text_message


def get_stock_notify():
    print('測試')
