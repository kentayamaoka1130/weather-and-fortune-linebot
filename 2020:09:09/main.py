from flask import Flask, request, abort
import os
import fortune_weather as fw

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#LINEでのイベントを取得
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#アプリケーション本体をopenすると実行される
@app.route("/")
def hello_world():
    return "hello world!"

#/callback　のリンクにアクセスしたときの処理。webhook用。
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
        abort(400)

    return 'OK'

#メッセージ受信時のイベント
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    '''
    #line_bot_apiのreply_messageメソッドでevent.message.text(ユーザのメッセージ)を返信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    '''
    a=event.message.text
    res=fw.fortune_weather(a)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=res)
    )

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)