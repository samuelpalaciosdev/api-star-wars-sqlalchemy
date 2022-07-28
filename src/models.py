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
            # do not serialize password for security purposes
        }
