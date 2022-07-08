from application import app 
from flask_testing import TestCase
from flask import url_for
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_get_front(self):
        with requests_mock.Mocker() as m:
            m.get('http://rand-name-gen:5000/get_name', text = 'abc')
            m.get('http://rand-num-gen:5000/get_nums', text = '120')
            m.post('http://race-gen:5000/get_race', text = 'Elf')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Elf', response.data)