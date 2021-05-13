# modules
from push.telegram import telegram_bot_sendimage, telegram_bot_sendtext
from push.twitter import tweet_image
import requests  # main thing     # get the keys
from dotenv import load_dotenv
import os                            # getenv
import json
import time

from tools.img import img_download
from push import *


load_dotenv()
newsapi_key = os.getenv("NEWSAPI_KEY")

# Get news

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=')

url += newsapi_key


try:
    response = requests.get(url)
except:
    print("Can't connect")

news = json.loads(response.text)


for new in news['articles']:
    author = (str(new['source']['name']))
    title = (str(new['title']))
    description = (str(new['description']))
    if description == None:
        description = ""
    image_url = (str(new['urlToImage']))
    full_story = (str(new['url']))

    # Telggram
    telegram_messge = "From " + author + "\n \n" + title + "\n \n" + description + "\n \n" + \
        "[Full Story]({})".format(full_story)

    telegram_bot_sendimage(image_url, telegram_messge)

    # Twitter

    twitter_message = "From " + author + "\n \n" + title + "\n \n" + \
        "Full story: " + url

    tweet_image(image_url, twitter_message)

    time.sleep(10)
