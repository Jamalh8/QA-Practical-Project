from application import app
from flask import request

@app.route('/rating', methods=['POST'])
def rating():
    rating = 150
    data_sent = request.get_json()
    #Driver rating
    if data_sent['driver'] == 'Max Verstappen':
        rating += 50
    if data_sent['driver'] == 'Lewis Hamilton':
        rating += 40
    if data_sent['driver'] == 'George Russell':
        rating += 45
    if data_sent['driver'] == 'Charles Leclerc':
        rating += 35
    if data_sent['driver'] == 'Sebastian Vettel':
        rating += 30
    if data_sent['driver'] == 'Fernando Alonso':
        rating += 25
    if data_sent['driver'] == 'Carlos Sainz Jr.':
        rating += 20
    if data_sent['driver'] == 'Sergio Perez':
        rating += 15
    if data_sent['driver'] == 'Lando Norris':
        rating += 20
    if data_sent['driver'] == 'Daniel Ricciardo':
        rating += 5
    if data_sent['driver'] == 'Valtteri Bottas':
        rating += 10
    if data_sent['driver'] == 'Guanyu Zhou':
        rating += 0
    if data_sent['driver'] == 'Pierre Gasly':
        rating += 20
    if data_sent['driver'] == 'Yuki Tsunoda':
        rating += -5
    if data_sent['driver'] == 'Esteban Ocon':
        rating += 5
    if data_sent['driver'] == 'Lance Stroll':
        rating += -25
    if data_sent['driver'] == 'Mick Schumacher':
        rating += -10
    if data_sent['driver'] == 'Kevin Magnussen':
        rating += 15
    if data_sent['driver'] == 'Alex Albon':
        rating += 10
    if data_sent['driver'] == 'Nicholas Latifi':
        rating += -30
    # Car rating
    if data_sent['car'] == 'Alfa Romeo Racing':
        rating += 25
    if data_sent['car'] == 'AlphaTauri-Red Bull':
        rating += 20
    if data_sent['car'] == 'Alpine-Renault':
        rating += 30
    if data_sent['car'] == 'Aston Martin':
        rating += 15
    if data_sent['car'] == 'Ferrari':
        rating += 45
    if data_sent['car'] == 'Haas-Ferrari':
        rating += 10
    if data_sent['car'] == 'McLaren-Mercedes':
        rating += 35 
    if data_sent['car'] == 'Mercedes-AMG':
        rating += 40
    if data_sent['car'] == 'Red Bull Racing':
        rating += 50
    if data_sent['car'] == 'Williams-Mercedes':
        rating += 5
    return str(rating)