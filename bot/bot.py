from time import sleep

import requests
import telebot

TOKEN = '742584960:AAEgQpt1c67yyWrZ_QC7L2XVtnvf3iq03oc'
CHANNEL_NAME = '@testmemespizdilovka01'

bot = telebot.TeleBot(TOKEN)
# bot.config['api_key'] = TOKEN

proxies = {
    'http': 'http://109.167.250.8:46610',
    'https': 'https://90.84.240.81:3128'
}


def _download_pic(name, pic_url):
    with open(name, 'wb') as handle:
        response = requests.get(pic_url, stream=True, proxies=proxies)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)


def _send_message(post):
    img_url = post.img
    _download_pic('./img.jpeg', img_url)
    photo = open('./img.jpeg', 'rb')
    bot.send_photo(CHANNEL_NAME, photo, post.text)


def send_posts(posts):
    for post in posts:
        _send_message(post)
        sleep(1800)
