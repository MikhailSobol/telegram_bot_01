import datetime


def g_memes(t):
    if t < 20:
        return 0.1
    elif 20 <= t <= 100:
        return 0.01
    return 0


def g_general(t):
    if t <= 750:
        return 0.2
    elif 750 < t < 1300:
        return 0.15
    return 0.1


def recency(r):
    if r < 1:
        return 0.05
    elif 3 <= r <= 7:
        return 0.025
    return 0.01


def _calculate_the_rating(post, q, g, f):
    return q * post.likes / post.views + g(len(post.text.split())) \
           + f((datetime.datetime.now() - post.date).days)


def sort_posts(posts, posts_type):
    q = 0.9 if posts_type == 'MEME' else 0.75
    _g = g_memes if posts_type == 'MEME' else g_general
    for post in posts:
        post.rating = _calculate_the_rating(post, q, _g, recency)
    posts = filter(lambda x: (datetime.datetime.now() - x.date).days < 1, posts)
    return sorted(posts, key=lambda x: x.rating, reverse=True)
