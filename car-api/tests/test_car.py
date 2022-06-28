from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCar(TestBase):
    @patch('application.routes.random.choice', return_value='McLaren-Mercedes')
    def test_get_car_1(self, patched):
        response =self.client.get(url_for('get_car'))
        self.assert200(response)
        self.assertIn(b'McLaren-Mercedes', response.data)

    @patch('application.routes.random.choice', return_value='Aston Martin')
    def test_get_car_2(self,patched):
        response =self.client.get(url_for('get_car'))
        self.assert200(response)
        self.assertIn(b'Aston Martin', response.data)

    @patch('application.routes.random.choice', return_value='Haas-Ferrari')
    def test_get_car_3(self,patched):
        response =self.client.get(url_for('get_car'))
        self.assert200(response)
        self.assertIn(b'Haas-Ferrari', response.data)

    @patch('application.routes.random.choice', return_value='Red Bull Racing')
    def test_get_car_4(self,patched):
        response =self.client.get(url_for('get_car'))
        self.assert200(response)
        self.assertIn(b'Red Bull Racing', response.data)

    @patch('application.routes.random.choice', return_value='Williams-Mercedes')
    def test_get_car_5(self,patched):
        response =self.client.get(url_for('get_car'))
        self.assert200(response)
        self.assertIn(b'Williams-Mercedes', response.data)

