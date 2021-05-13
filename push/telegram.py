from logging import captureWarnings
import requests
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")


def telegram_bot_sendtext(bot_message):

    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id=@savethatnews&disable_web_page_preview=false&"
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()


def telegram_bot_sendimage(url, caption):
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendPhoto?chat_id=@savethatnews&disable_web_page_preview=false&"
        + "&photo="
        + url
        + "&parse_mode=Markdown&caption="
        + caption
    )

    response = requests.get(send_text)

    return response.json()
