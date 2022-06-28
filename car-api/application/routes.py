from application import app
import random

@app.route('/get_car', methods=['GET'])
def get_car():
    cars = ['Alfa Romeo Racing', 'AlphaTauri-Red Bull', 'Alpine-Renault','Aston Martin',
        'Ferrari', 'Haas-Ferrari', 'McLaren-Mercedes', 'Mercedes-AMG', 'Red Bull Racing',
        'Williams-Mercedes']
    car = random.choice(cars)
    return car
