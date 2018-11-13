import datetime
from time import sleep

import requests

from parser.parser import get_posts
from analyzer.analyzer import sort_posts
from bot.bot import send_posts


if __name__ == '__main__':
    while True:
        current_date = datetime.datetime.now()

        posts_1 = get_posts('-460389', 100)
        posts_2 = get_posts('-57846937', 100)
        posts = sort_posts([*posts_1, *posts_2], posts_type='MEME')[3:43]
        send_posts(posts)

        # send_posts
        while (datetime.datetime.now() - current_date).days == 0:
            sleep(60)
