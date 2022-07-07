from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

#Testing home page upon user arrival
class TestRatings(TestBase):
    def test_get_rating1(self):
        response = self.client.post(url_for('rating'), json={"driver": "Max Verstappen", "car": "Alfa Romeo Racing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'225', response.data)
        
    def test_get_rating2(self):
        response = self.client.post(url_for('rating'), json={"driver": "Lewis Hamilton", "car": "AlphaTauri-Red Bull"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'210', response.data)

    def test_get_rating3(self):
        response = self.client.post(url_for('rating'), json={"driver": "George Russell", "car": "Alpine-Renault"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'225', response.data)

    def test_get_rating4(self):
        response = self.client.post(url_for('rating'), json={"driver": "Charles Leclerc", "car": "Aston Martin"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'200', response.data)

    def test_get_rating5(self):
        response = self.client.post(url_for('rating'), json={"driver": "Sebastian Vettel", "car": "Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'225', response.data)

    def test_get_rating6(self):
        response = self.client.post(url_for('rating'), json={"driver": "Fernando Alonso", "car": "Haas-Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'185', response.data)

    def test_get_rating7(self):
        response = self.client.post(url_for('rating'), json={"driver": "Carlos Sainz Jr.", "car": "McLaren-Mercedes"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'205', response.data)

    def test_get_rating8(self):
        response = self.client.post(url_for('rating'), json={"driver": "Sergio Perez", "car": "Mercedes-AMG"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'205', response.data)

    def test_get_rating9(self):
        response = self.client.post(url_for('rating'), json={"driver": "Lando Norris", "car": "Red Bull Racing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'220', response.data)

    def test_get_rating10(self):
        response = self.client.post(url_for('rating'), json={"driver": "Daniel Ricciardo", "car": "Williams-Mercedes"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'160', response.data)

    def test_get_rating11(self):
        response = self.client.post(url_for('rating'), json={"driver": "Valtteri Bottas", "car": "Alfa Romeo Racing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'185', response.data)

    def test_get_rating12(self):
        response = self.client.post(url_for('rating'), json={"driver": "Guanyu Zhou", "car": "AlphaTauri-Red Bull"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'170', response.data)

    def test_get_rating13(self):
        response = self.client.post(url_for('rating'), json={"driver": "Pierre Gasly", "car": "Alpine-Renault"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'200', response.data)

    def test_get_rating14(self):
        response = self.client.post(url_for('rating'), json={"driver": "Yuki Tsunoda", "car": "Aston Martin"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'160', response.data)

    def test_get_rating15(self):
        response = self.client.post(url_for('rating'), json={"driver": "Esteban Ocon", "car": "Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'200', response.data)

    def test_get_rating16(self):
        response = self.client.post(url_for('rating'), json={"driver": "Lance Stroll", "car": "Haas-Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'135', response.data)

    def test_get_rating17(self):
        response = self.client.post(url_for('rating'), json={"driver": "Mick Schumacher", "car": "McLaren-Mercedes"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'175', response.data)

    def test_get_rating18(self):
        response = self.client.post(url_for('rating'), json={"driver": "Kevin Magnussen", "car": "Mercedes-AMG"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'205', response.data)

    def test_get_rating19(self):
        response = self.client.post(url_for('rating'), json={"driver": "Alex Albon", "car": "Red Bull Racing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'210', response.data)

    def test_get_rating20(self):
        response = self.client.post(url_for('rating'), json={"driver": "Nicholas Latifi", "car": "Williams-Mercedes"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'125', response.data)

    def test_get_rating21(self):
        response = self.client.post(url_for('rating'), json={"driver": "Ayrton Senna", "car": "Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'245', response.data)

    def test_get_rating22(self):
        response = self.client.post(url_for('rating'), json={"driver": "Niki Lauda", "car": "Haas-Ferrari"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'195', response.data)

    def test_get_rating23(self):
        response = self.client.post(url_for('rating'), json={"driver": "Mick Schumacher", "car": "McLaren-Mercedes"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'225', response.data)

    def test_get_rating24(self):
        response = self.client.post(url_for('rating'), json={"driver": "Nigel Mansell", "car": "Mercedes-AMG"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'230', response.data)

    def test_get_rating25(self):
        response = self.client.post(url_for('rating'), json={"driver": "Martin Brundle", "car": "Red Bull Racing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'230', response.data)