from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, User, Character, Planet, Vehicle

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

#### code inside this lines ####

@app.route('/')
def main():
    return jsonify({ "msg": "Welcome to Star Wars API!!!" }), 200

#### code inside this lines ####
if __name__ == '__main__':
    app.run()