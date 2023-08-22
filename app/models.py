from sqlalchemy import (
    Integer,
    Column,
    Text,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

# App imports
from app import db_manager

Base = db_manager.Model


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    premiere = Column(DateTime, nullable=True)
    director = Column(Text, nullable=False)
    countries = relationship("Country", back_populates="movies")
    genres = relationship("Genre", back_populates="movies")
    actors = relationship("Actor", back_populates="movies")


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class MovieCountry(Base):
    __tablename__ = "movies_x_countries"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    country_id = Column(Integer, ForeignKey("countries.id"), primary_key=True)
    assigned_at = Column(DateTime, nullable=False, server_default=func.now())


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class MovieGenre(Base):
    __tablename__ = "movies_x_genres"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    Genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)
    assigned_at = Column(DateTime, nullable=False, server_default=func.now())


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class MovieActor(Base):
    __tablename__ = "movies_x_actors"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)
    assigned_at = Column(DateTime, nullable=False, server_default=func.now())
