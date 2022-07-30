from crypt import methods
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, User, Character, Planet, Vehicle, favorite_characters, favorite_planets, favorite_vehicles

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

#### Main Route ####

@app.route('/') 
def main():
    return jsonify({ "msg": "Welcome to Star Wars API!!!" }), 200

#### Characters Route ####

# Returns list of all the characters in the Database
@app.route('/api/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(characters), 200

# Returns info about a character by id
@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    character = Character.query.get(character_id)
    return jsonify(character.serialize()), 200


#### Planets Route ####

# Returns list of all the planets in the Database
@app.route('/api/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

# Returns info about a planet by id
@app.route('/api/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify(planet.serialize()), 200

#### Vehicles Route ####

# Returns list of all the vehicles in the Database
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))
    return jsonify(vehicles), 200

# Returns info about a vehicle by id
@app.route('/api/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    return jsonify(vehicle.serialize()), 200

#### Users Route ####

# Returns list of all the users in the Database
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200



#### code inside this lines ####
if __name__ == '__main__':
    app.run()