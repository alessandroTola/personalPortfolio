class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        rep = 'Post(' + self.title + ', ' + self.content + ')'
        return rep

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
