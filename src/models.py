import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Enum, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)
    profile_pic = Column(String(250), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    date_of_birth = Column(Date, nullable=True)
    phone_number = Column(String(10), nullable=True)
    account_status =Column(Enum('activa', 'eliminada', 'suspendida', name='account_status'), nullable=False)

class Role(Base):
    __tablename__='role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    activity_type = Column(Enum('Planet_activity', 'People_activity'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    favorite = Column(Boolean, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class People(Base):
    __tablename__='people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(10), nullable=False)
    eye_color= Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    hair_color = Column(String(10), nullable=False)
    height = Column(String(10), nullable=False)
    mass = Column(String(10), nullable=False)
    skin_color = Column(String(10), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class Film(Base):
    __tablename__='film'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl=Column(String(250), nullable=False)
    director = Column(String(50), nullable=False)
    producer = Column(String(100), nullable=False)
    realase_date = Column(Date, nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class Planet (Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(20), nullable=False)
    rotation_period = Column(String(10), nullable=False)
    orbital_period = Column(String(10), nullable=False)
    gravity = Column(String(20), nullable=False)
    population = Column(String(20), nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(10), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class Specie(Base):
    __tablename__='specie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    classification = Column(String(20), nullable=False)
    designation = Column(String(20), nullable=False)
    average_height = Column(String(10), nullable=False)
    average_lifespan = Column(String(10), nullable=False)
    eye_colors = Column(String(100), nullable=False)
    hair_colors = Column(String(100), nullable=False)
    skin_color = Column(String(100), nullable=False)
    language = Column(String(15), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'), nullable=True)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class Vehicle(Base):
    __tablename__='vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(20), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    length = Column(String(10), nullable=False)
    cost_in_credits = Column(String(20), nullable= False)
    crew = Column(String(10), nullable=False)
    passengers = Column(String(10), nullable=False)
    max_atmosphering_speed = Column(String(10), nullable=False)
    cargo_capacity = Column(String(10), nullable=False)
    consumables = Column(String(20), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class Starship(Base):
    __tablename__='starship'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(100), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(20), nullable= False)
    length = Column(String(10), nullable=False)
    crew = Column(String(10), nullable=False)
    passengers = Column(String(10), nullable=False)
    max_atmosphering_speed = Column(String(10), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    mglt = Column(String(20), nullable=False)       
    cargo_capacity = Column(String(10), nullable=False)
    consumables = Column(String(20), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(20), nullable = False)
    edited = Column(String(20), nullable = False)

class PeopleFilms(Base):
    __tablename__='people_films'
    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)

class PeopleSpecies(Base):
    __tablename__='people_species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    specie_id = Column(Integer, ForeignKey('specie.id'), nullable=False)

class PeopleStarships(Base):
    __tablename__='people_starships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=False)

class PeopleVehicles(Base):
    __tablename__='people_vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)

class PlanetsPeople(Base):
    __tablename__='planet_people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    
class FilmsSpecies(Base):
    __tablename__='films_species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    specie_id = Column(Integer, ForeignKey('specie.id'), nullable=False)

class FilmsStarships(Base):
    __tablename__='film_starships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=False)

class FilmsVehicles(Base):
    __tablename__='film_vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)

class FilmsPlanets(Base):
    __tablename__='film_planets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
