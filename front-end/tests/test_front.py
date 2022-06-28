from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

#Testing home page upon user arrival
class TestFrontViewIndex(TestBase):
    def test_get_front(self):
            response =self.client.get(url_for('index'))
            self.assert200(response)

#Testing to see if anyone just goes directly to Generate on Load it'll give error 500
class TestFrontViewGenerate(TestBase):
    def test_get_front(self):
            response =self.client.get(url_for('generate'))
            self.assert500(response)

#Test driver 1
class TestFrontGenerator1(TestBase):
    def test_get_front_generate1(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_driver', text='Lewis Hamilton')
            m.get('http://service_3:5000/get_car', text='Haas-Ferrari')
            m.post('http://service_4:5000/rating', text='200')
            response =self.client.get(url_for('generate'))
            self.assert200(response)
            self.assertIn(b'Lewis Hamilton', response.data)
            self.assertIn(b'Haas-Ferrari', response.data)
            self.assertIn(b'200', response.data)

#Test driver 2
class TestFrontGenerator2(TestBase):
    def test_get_front_generate2(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_driver', text='Max Verstappen')
            m.get('http://service_3:5000/get_car', text='Red Bull Racing')
            m.post('http://service_4:5000/rating', text='250')
            response =self.client.get(url_for('generate'))
            self.assert200(response)
            self.assertIn(b'Max Verstappen', response.data)
            self.assertIn(b'Red Bull Racing', response.data)
            self.assertIn(b'250', response.data)

#Test driver 3   
class TestFrontGenerator3(TestBase):
    def test_get_front_generate3(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_driver', text='George Russell')
            m.get('http://service_3:5000/get_car', text='Alfa Romeo Racing')
            m.post('http://service_4:5000/rating', text='220')
            response =self.client.get(url_for('generate'))
            self.assert200(response)
            self.assertIn(b'George Russell', response.data)
            self.assertIn(b'Alfa Romeo Racing', response.data)
            self.assertIn(b'220', response.data)

#Test driver 4
class TestFrontGenerator4(TestBase):
    def test_get_front_generate4(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_driver', text='Charles Leclerc')
            m.get('http://service_3:5000/get_car', text='Ferrari')
            m.post('http://service_4:5000/rating', text='230')
            response =self.client.get(url_for('generate'))
            self.assert200(response)
            self.assertIn(b'Charles Leclerc', response.data)
            self.assertIn(b'Ferrari', response.data)
            self.assertIn(b'230', response.data)

#Test driver 5
class TestFrontGenerator5(TestBase):
    def test_get_front_generate5(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_driver', text='Sebastian Vettel')
            m.get('http://service_3:5000/get_car', text='Aston Martin')
            m.post('http://service_4:5000/rating', text='195')
            response =self.client.get(url_for('generate'))
            self.assert200(response)
            self.assertIn(b'Sebastian Vettel', response.data)
            self.assertIn(b'Aston Martin', response.data)
            self.assertIn(b'195', response.data)

