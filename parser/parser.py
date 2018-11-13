from datetime import datetime
from model.Post import Post
import requests

proxies = {
    'http': 'http://109.167.250.8:46610',
    'https': 'https://90.84.240.81:3128'
}

TOKEN = '82c0c30282c0c30282c0c302de82a624a1882c082c0c302d922c6c1dfc0f611c7faf47c'
VAPI = '5.87'


def get_posts(group_id, post_count=100, offset=0):
    return _extract_useful_info(_get_posts(group_id, post_count, offset))


def _get_posts(group_id, post_count, offset=0):
    url = 'https://api.vk.com/method/wall.get?owner_id=' + \
          group_id + '&access_token=' + TOKEN + '&v=' + VAPI + \
          '&count=' + str(post_count) + '&offset=' + str(offset)
    return requests.get(url, proxies=proxies).json()['response']['items']


def _extract_useful_info(posts):
    filtered = []
    for post in posts:
        is_ad = post['marked_as_ads']
        if is_ad:
            continue
        text = post['text']
        if len(text) > 1000:
            continue
        views = post['views']['count']
        likes = post['likes']['count']
        date = datetime.utcfromtimestamp(post['date'])
        try:
            img = post['attachments'][0]['photo']['sizes'][4]['url']
        except KeyError:
            continue
        filtered.append(Post(text, img, date, views, likes))
    return filtered


if __name__ == '__main__':
    posts = get_posts('-131518333', 2)
    for post in posts:
        print(post.date)
