from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True  # we are telling to Flask that is in testing mode
        self.app = app.test_client
