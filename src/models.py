from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
db = SQLAlchemy() 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False) 
    is_active = db.Column(db.Boolean(), nullable=False) # check if user is connected

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'is_active': self.is_active
            # do not serialize password for security purposes
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(250), default="https://www.prensalibre.com/wp-content/uploads/2019/11/luke-skywalker-644x362.jpg?quality=52")
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    # homeworld = db.Column(db.Integer, ForeignKey('planets.id'), default='unknown')

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth-year': self.birth_year,
            'gender': self.gender
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    picture = db.Column(db.String(250), default="https://static.wikia.nocookie.net/starwars/images/9/98/Taris_TOR.png/revision/latest?cb=20190421041041")
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(100), default="unknown")
    gravity = db.Column(db.String(50), default="unknown")
    terrain = db.Column(db.String(100), default="unknown")
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    characters_born_here = db.relationship('Character', backref='planet')

    def serialize(self): 
        return {
            'id': self.id,
            'name': self.name,
            'picture': self.picture,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population
        }

    