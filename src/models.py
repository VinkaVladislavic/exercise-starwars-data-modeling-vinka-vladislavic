import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, BigInteger, Float
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    subscription_date = Column(Date, nullable=False)

    login = relationship("Login", back_populates="user")
    favorite_planets = relationship("FavoritePlanet", back_populates="user")
    favorite_characters = relationship("FavoriteCharacter", back_populates="user")
    favorite_vehicles = relationship("FavoriteVehicle", back_populates="user")

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False) 

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="login")

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    character = relationship("Character")
    vehicle = relationship("Vehicle")

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(BigInteger, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Float, nullable=False)
    terrain = Column(String(250))
    surface_water = Column(Float, nullable=False)
    climate = Column(String(250))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    species = Column(String(250))
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    class_vehicle = Column(String(250))
    cost = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    length = Column(Float, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    minimum_crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet")

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character")

class FavoriteVehicle(Base):
    __tablename__ = 'favorite_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

    user = relationship("User", back_populates="favorite_vehicles")
    vehicle = relationship("Vehicle")    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
