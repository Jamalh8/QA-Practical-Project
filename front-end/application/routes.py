from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    driver = requests.get('http://service_2:5000/get_driver').text
    car = requests.get('http://service_3:5000/get_car').text
    rating = requests.post('http://service_4:5000/rating', json=dict(driver=driver,car=car))
    return render_template('home.html', driver=driver, car=car, rating=rating.text )