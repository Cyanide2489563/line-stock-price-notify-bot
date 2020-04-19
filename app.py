from flask import Flask, request, abort
from linebot import WebhookHandler, LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, MessageAction, QuickReplyButton, QuickReply

import Config
import stock_api
import stock_message
from database.database import create_database

from database.sqlite.sqlite_api import add_user_stock

app = Flask(__name__)

line_bot_api = LineBotApi(Config.get_channel_access_token())
handler = WebhookHandler(Config.get_channel_secret())


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    create_database()
    if event.source.type != 'user':
        line_bot_api.reply_message(event.reply_token, TextSendMessage('目前僅支援一對一聊天功能'))

    message = event.message.text.split(':')
    stock_id = message[0]
    command = ''
    if len(message) == 2:
        command = message[1]
    if command == '查看圖表':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(event.source.user_id + '此功能尚未開放'))
    if command == '加入我的股票':
        add_user_stock(event.source.user_id, stock_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請輸入股票代碼'))

    if stock_api.is_stock(stock_id):
        line_bot_api.reply_message(event.reply_token, stock_message.get_stock_info(stock_id))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('股票代碼錯誤'))


if __name__ == '__main__':
    app.run()
