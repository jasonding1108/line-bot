##架設伺服器: flask(程式), django(網頁)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, AudioSendMessage, VideoSendMessage
)

app = Flask(__name__)


#acess token
line_bot_api = LineBotApi('XEqbRkG/MVu3YPzPTwM0M3s6OPnyRNELH5jTVDq+F/HT6ECx8hTcGEy6F5UFRlO2RO8g580gTQC2xaUgGSlRx2eF6Iy4uiNtvgrGO82e1xgJmUIZylNQ324t0MRiIPnJRFSLkPg4z68oW8uehdj9EwdB04t89/1O/w1cDnyilFU=')

#channel secret
handler = WebhookHandler('e9bc0e98ac906434d52327b31c910382')


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
    msg = event.message.text
    r = '很抱歉, 您說甚麼'

    if "給我貼圖" in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
            event.reply_token, sticker_message)
        return

    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))

if __name__ == "__main__":
    app.run()