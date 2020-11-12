from anime_flask import app
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_marshmallow import Marshmallow
import os
from flask_jwt_extended import JWTManager, jwt_required, create_access_token  
from flask_mail import Mail, Message

# Put data file in same path as app file
basedir =  os.path.abspath(os.path.dirname(__file__))
basedir = basedir[:-14]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Data/sqlite/planets.db')
app.config['JWT_SECRET_KEY'] = 'super-secret' # CHange this IRL
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '6fede7a320205b'
app.config['MAIL_PASSWORD'] = '21f158aaff91df'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)

# Constructor class for database model
class User(db.Model):
    __table_name__ = 'users'
    username = Column(String, unique=True)
    id = Column(Integer, primary_key=True)
    user_watching = Column(Integer)
    user_completed = Column(Integer)
    user_dropped = Column(Integer)
    user_plantowatch = Column(Integer)
    user_days_spent_watching = Column(Float)
    gender = Column(String)
    location = Column(String)
    birth_date = Column(String)
    join_date = Column(String)
    stats_mean_score = Column(Float)
    stats_rewatched = Column(Float)
    stats_episodes = Column(Float)
    email = Column(String, unique=True)
    password = Column(String)
    
class Planet(db.Model):
    __table_name__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

class UserSchema(ma.Schema):
    class Meta:
        fields=('id', 'username', 'gender', 'location', 'user_watching', 'user_completed', 'user_dropped', 'user_plantowatch', 'user_days_spent_watching', 'birth_date', 'join_date', 'stats_mean_score', 'stats_rewatched', 'stats_episodes')
        
class PlanetSchema(ma.Schema):
    class Meta:
        fields=('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)