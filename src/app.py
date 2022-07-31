from re import S
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

# Returns list of all the characters in the Database and Create Character
@app.route('/characters', methods=['GET', 'POST'])
def list_and_create_character():

    if request.method == 'GET':
        characters = Character.query.all()
        characters = list(map(lambda character: character.serialize(), characters))
        return jsonify(characters), 200
    
    if request.method == 'POST':

        data = request.get_json()

        character = Character()
        character.name = data['name']
        character.image = data['image']
        character.height = data['height']
        character.mass = data['mass']
        character.hair_color = data['hair_color']
        character.skin_color = data['skin_color']
        character.eye_color = data['eye_color']
        character.birth_year = data['birth_year']
        character.gender = data['gender']

        character.save()

        return jsonify(character.serialize()), 201


# Returns info about a character by id
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    character = Character.query.get(character_id)
    return jsonify(character.serialize()), 200


#### Planets Route ####

# Returns list of all the planets in the Database and Create Planet
@app.route('/planets', methods=['GET', 'POST'])
def list_and_create_planets():

    if request.method == 'GET':
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify(planets), 200    

    if request.method == 'POST':
        data = request.get_json()
        planet = Planet()  
        planet.name = data['name']
        planet.image = data['image']
        planet.rotation_period = data['rotation_period']
        planet.orbital_period = data['orbital_period']
        planet.diameter = data['diameter']
        planet.climate = data['climate']
        planet.gravity = data['gravity']
        planet.terrain = data['terrain']
        planet.surface_water = data['surface_water']
        planet.population = data['population']
        planet.save()

        return jsonify(planet.serialize()), 201


# Returns info about a planet by id
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify(planet.serialize()), 200

#### Vehicles Route ####

# Returns list of all the vehicles in the Database and Create Vehicle
@app.route('/vehicles', methods=['GET', 'POST'])
def list_and_create_vehicles():
    if request.method == 'GET':
        vehicles = Vehicle.query.all()
        vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))
        return jsonify(vehicles), 200

    if request.method == 'POST':
        data = request.get_json()
        vehicle = Vehicle()
        vehicle.name = data['name']
        vehicle.image = data['image']
        vehicle.model = data['model']
        vehicle.manufacturer = data['manufacturer']
        vehicle.cost_in_credits = data['cost_in_credits']
        vehicle.length = data['length']
        vehicle.max_atmosphering_speed = data['max_atmosphering_speed']
        vehicle.crew = data['crew']
        vehicle.passengers = data['passengers']
        vehicle.cargo_capacity = data['cargo_capacity']
        vehicle.consumables = data['consumables']
        vehicle.vehicle_class = data['vehicle_class']
        vehicle.save()

        return jsonify(vehicle.serialize()), 201


# Returns info about a vehicle by id
@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
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


######################## USER FAVORITES HERE

# Returns user favorites list
@app.route('/users/<int:user_id>/favorites/', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.get(user_id)
    message = {
        "User": user.name,
        "Favorite Characters": list(map(lambda character: character.serialize(), user.fav_characters)),
        "Favorite Planets": list(map(lambda planet: planet.serialize(), user.fav_planets)),
        "Favorite Vehicles": list(map(lambda vehicle: vehicle.serialize(), user.fav_vehicles))
    }
    return jsonify(message), 200

# Add or Delete Favorite Character
@app.route('/users/<int:user_id>/favorites/characters/<int:character_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_character(user_id,character_id):
    # Add favorite character
    if request.method == 'POST':
        # Get the user based on the param user_id of the route
        user = User.query.get(user_id)
        username = request.json.get('username')
        character_id = Character.query.get(character_id)

        # if the character_id passed as a param to the route is not in the fav_characters list of the user, then add it
        if not character_id in user.fav_characters:
            user.fav_characters.append(character_id)

        user.update()
        return jsonify(user.serialize()), 201
        
    # Delete favorite character based on the character_id param passed to the route
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        username = request.json.get('username')
        character_id = Character.query.get(character_id)

        user.fav_characters.remove(character_id)

        user.update()
        return jsonify(user.serialize()), 200
        
# Add or Delete Favorite Planet
@app.route('/users/<int:user_id>/favorites/planets/<int:planet_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_planet(user_id,planet_id):
    # Add favorite Planet
    if request.method == 'POST':
        # Get the user based on the param user_id of the route
        user = User.query.get(user_id)
        username = request.json.get('username')
        planet_id = Planet.query.get(planet_id)

        # if the planet_id passed as a param to the route is not in the fav_planets list of the user, then add it
        if not planet_id in user.fav_planets:
            user.fav_planets.append(planet_id)

        user.update()
        return jsonify(user.serialize()), 201
        
    # Delete favorite Planet
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        username = request.json.get('username')
        planet_id = Planet.query.get(planet_id)

        user.fav_planets.remove(planet_id )

        user.update()
        return jsonify(user.serialize()), 200

# Add or Delete Favorite Vehicle
@app.route('/users/<int:user_id>/favorites/vehicles/<int:vehicle_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_vehicle(user_id,vehicle_id):
    # Add favorite Vehicle
    if request.method == 'POST':
        # Get the user based on the param user_id of the route
        user = User.query.get(user_id)
        username = request.json.get('username')
        vehicle_id = Vehicle.query.get(vehicle_id)

        # if the vehicle_id passed as a param to the route is not in the fav_vehicles list of the user, then add it
        if not vehicle_id in user.fav_vehicles:
            user.fav_vehicles.append(vehicle_id)

        user.update()
        return jsonify(user.serialize()), 201
        
    # Delete favorite Vehicle
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        username = request.json.get('username')
        vehicle_id = Vehicle.query.get(vehicle_id)

        user.fav_vehicles.remove(vehicle_id )

        user.update()
        return jsonify(user.serialize()), 200


#### code inside this lines ####
if __name__ == '__main__':
    app.run()

