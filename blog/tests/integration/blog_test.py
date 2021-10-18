from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b1 = Blog('Test', 'Test Author')
        b1.create_post('Test post', 'Test Content')

        self.assertEqual(len(b1.posts), 1)
        self.assertEqual(b1.posts[0].title, 'Test post')
        self.assertEqual(b1.posts[0].content, 'Test Content')

    def test_json_no_posts(self):
        b1 = Blog('Test', 'Test Author')
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []
        }

        self.assertDictEqual(expected, b1.json())

    def test_json(self):
        b1 = Blog('Test', 'Test Author')
        b1.create_post('Test post', 'Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test post',
                    'content': 'Test Content'
                }
            ]
        }

        self.assertDictEqual(expected, b1.json())
