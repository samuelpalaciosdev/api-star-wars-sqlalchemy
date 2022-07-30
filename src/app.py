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

#### code inside this lines ####

@app.route('/') # Main Page
def main():
    return jsonify({ "msg": "Welcome to Star Wars API!!!" }), 200

# Returns list of all the characters in the Database
@app.route('/api/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(characters), 200


# Returns info about a character based on its id

@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    characters = Character.query.get(character_id)
    return jsonify(characters.serialize()), 200




#### code inside this lines ####
if __name__ == '__main__':
    app.run()