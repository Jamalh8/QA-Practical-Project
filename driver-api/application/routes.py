from application import app
import random

@app.route('/get_driver', methods=['GET'])
def get_driver():
    drivers = ['Valtteri Bottas', 'Guanyu Zhou', 'Pierre Gasly', 'Yuki Tsunoda', 'Fernando Alonso', 
    'Esteban Ocon', 'Sebastian Vettel', 'Lance Stroll', 'Charles Leclerc', 'Carlos Sainz Jr.', 
    'Mick Schumacher', 'Kevin Magnussen', 'Daniel Ricciardo', 'Lando Norris', 'Lewis Hamilton', 
    'George Russell', 'Max Verstappen', 'Sergio Perez', 'Alex Albon', 'Nicholas Latifi', 'Ayrton Senna', 'Niki Lauda', 'Nigel Mansell', 'Michael Schumacher', 'Martin Brundle']
    driver = random.choice(drivers)
    return driver

