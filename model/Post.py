class Post:
    def __init__(self, text, img, date, views, likes):
        self.text = text
        self.img = img
        self.date = date
        self.views = views
        self.likes = likes
        self.rating = None

    def __str__(self):
        return 'Post(text: {}, img: {}, date: {}, views: {}, likes={}, rating={})'.format(self.text[:50] + '..', self.img, self.date, self.views, self.likes, self.rating)
