from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    username: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(16), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    created: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="user")

class People(db.Model):
    __tablename__ = "people"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    birth_year: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    eye_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    gender: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    hair_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    height: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    mass: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    skin_color: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    homeworld: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    created: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="people")

class Vehicle(db.Model):
    __tablename__ = "vehicle"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    model: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    vehicle_class: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    speed: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    weight: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    length: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    created: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="vehicle")

class Planet(db.Model):
    __tablename__ = "planet"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    gravity: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    population: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    climate: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    terrain: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    created: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[int] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="planet")

class Favorite(db.Model):
	__tablename__ = "favorite"

	id: Mapped[int] = mapped_column(primary_key=True)
	user_id: Mapped[int] = mapped_column(Foreign_Key='user.id', nullable=False)
	people_id: Mapped[int] = mapped_column(Foreign_Key='people.id', nullable=False)
	vehicle_id: Mapped[int] = mapped_column(Foreign_Key='vehicle.id', nullable=False)
	planet_id: Mapped[int] = mapped_column(Foreign_Key='planet.id', nullable=False)