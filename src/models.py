from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
db = SQLAlchemy() 

favorite_characters = db.Table('favorite_characters',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key= True),
    db.Column('character_id', db.Integer, db.ForeignKey('characters.id'), primary_key=True)
)

favorite_planets = db.Table('favorite_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True)
)

favorite_vehicles = db.Table('favorite_vehicles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    fav_characters = db.relationship('Character', secondary='favorite_characters', backref='liked_by_user')
    fav_planets = db.relationship('Planet', secondary='favorite_planets', backref='liked_by_user')
    fav_vehicles = db.relationship('Vehicle', secondary='favorite_vehicles', backref='liked_by_user')
    is_active = db.Column(db.Boolean(), nullable=False) # check if user is connected

    def serialize(self):
        return{
            'id': self.id,
            'email': self.email,
            'is_active': self.is_active,
            'name': self.name,
            'last_name': self.last_name
            # do not serialize password for security purposes
        }
    
    def get_characters(self):
        return list(map(lambda character: character.serialize(), self.fav_characters))

    def get_planets(self):
        return list(map(lambda planet: planet.serialize(), self.fav_planets))

    def get_vehicles(self):
        return list(map(lambda vehicle: vehicle.serialize(), self.fav_vehicles))

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
    image = db.Column(db.String(250), default='https://www.prensalibre.com/wp-content/uploads/2019/11/luke-skywalker-644x362.jpg?quality=52')
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50), default='n/a')
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(50), default='n/a')
    # liked_by_user = db.relationship('User', secondary='favorite_characters')
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
    image = db.Column(db.String(250), default='https://static.wikia.nocookie.net/starwars/images/9/98/Taris_TOR.png/revision/latest?cb=20190421041041')
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(100), default='unknown')
    gravity = db.Column(db.String(50), default='unknown')
    terrain = db.Column(db.String(100), default='unknown')
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    # characters_born_here = db.relationship('Character', backref='planet')

    def serialize(self): 
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(250), default='https://cdn.drivingline.com/media/12940/dl-sw_10-06.jpg')
    model = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Float)
    max_atmospheric_speed = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(100))
    vehicle_class = db.Column(db.String(100))

    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'max_atmospheric_speed': self.max_atmospheric_speed,
            'crew': self.crew,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'vehicle_class': self.vehicle_class
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
