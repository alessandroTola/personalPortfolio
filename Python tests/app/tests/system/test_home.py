from tests.system.base_test import BaseTest
from http import HTTPStatus
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, HTTPStatus.OK)
            self.assertEqual(
                json.loads(resp.get_data()),
                {'message': 'Hello, world!'}
            )
