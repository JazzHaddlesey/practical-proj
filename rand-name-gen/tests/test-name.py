from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNames(TestBase):
    @patch('application.routes.names', return_value = 'abc')
    def test_get_name(self, patch):
        response = self.client.get(url_for('get_name'))
        self.assert500(response)
        self.assertIn(b'abc', response.data)