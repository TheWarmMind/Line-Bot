from flask import Flask, request
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(name)

line_bot_api = LineBotApi(os.getenv(”CHANNEL_ACCESS_TOKEN“))
handler = WebhookHandler(os.getenv(”CHANNEL_SECRET“))

@app.route(”/callback“, methods=[’POST‘])
def callback():
    signature = request.headers[’X-Line-Signature‘]
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return ’OK‘

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=”สวัสดี นี่คือบอทไลน์ 🤖“)
    )

if name == ”main“:
    app.run()
