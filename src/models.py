from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    username: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    created: Mapped[datetime] = mapped_column(DateTime,default=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")

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
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="people", cascade="all, delete-orphan")

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
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="vehicle", cascade="all, delete-orphan")

class Planet(db.Model):
    __tablename__ = "planet"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=False, nullable=False)
    gravity: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    population: Mapped[str] = mapped_column(String(16), unique=False, nullable=True)
    climate: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    terrain: Mapped[str] = mapped_column(String(128), unique=False, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    edited: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="planet", cascade="all, delete-orphan")

class Favorite(db.Model):
    __tablename__ = "favorite"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    people_id: Mapped[int] = mapped_column(ForeignKey('people.id'), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicle.id'), nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=True)

    user: Mapped["User"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")
    vehicle: Mapped["Vehicle"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")