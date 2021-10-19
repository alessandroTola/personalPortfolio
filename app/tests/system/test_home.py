from unittest import TestCase
from app import app
from http import HTTPStatus
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, HTTPStatus.OK)
            self.assertEqual(
                json.loads(resp.get_data()),
                {'message': 'Hello, world!'}
            )
