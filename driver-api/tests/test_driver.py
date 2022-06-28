from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDrivers(TestBase):
    @patch('application.routes.random.choice', return_value='Guanyu Zhou')
    def test_get_driver_1(self, patched):
        response =self.client.get(url_for('get_driver'))
        self.assert200(response)
        self.assertIn(b'Guanyu Zhou', response.data)

    @patch('application.routes.random.choice', return_value='Daniel Ricciardo')
    def test_get_driver_2(self,patched):
        response =self.client.get(url_for('get_driver'))
        self.assert200(response)
        self.assertIn(b'Daniel Ricciardo', response.data)

    @patch('application.routes.random.choice', return_value='Kevin Magnussen')
    def test_get_driver_3(self,patched):
        response =self.client.get(url_for('get_driver'))
        self.assert200(response)
        self.assertIn(b'Kevin Magnussen', response.data)

    @patch('application.routes.random.choice', return_value='Nicholas Latifi')
    def test_get_driver_4(self,patched):
        response =self.client.get(url_for('get_driver'))
        self.assert200(response)
        self.assertIn(b'Nicholas Latifi', response.data)

    @patch('application.routes.random.choice', return_value='Esteban Ocon')
    def test_get_driver_5(self,patched):
        response =self.client.get(url_for('get_driver'))
        self.assert200(response)
        self.assertIn(b'Esteban Ocon', response.data)

