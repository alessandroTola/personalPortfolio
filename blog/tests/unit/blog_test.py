from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, b.posts)

    def test_reps(self):
        b1 = Blog('Test', 'Test Author')
        b2 = Blog('Dove trovare il miglior vino', 'Diego Poddi')

        self.assertEqual(b1.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'Dove trovare il miglior vino by Diego Poddi (0 posts)')

    def test_multiple_posts(self):
        b1 = Blog('Test', 'Test Author')
        b2 = Blog('Dove trovare il miglior vino', 'Diego Poddi')

        b1.posts = ['My post']
        b2.posts = ['Dove trovare il miglior vino', 'Diego Poddi']

        self.assertEqual(b1.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Dove trovare il miglior vino by Diego Poddi (2 posts)')
