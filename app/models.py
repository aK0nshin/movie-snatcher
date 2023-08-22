from datetime import datetime

from sqlalchemy import (
    Integer,
    Column,
    Text,
    DateTime,
    ForeignKey,
    func, Table, inspect,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import db_manager

Base = db_manager.Model

movie_country = Table(
    "movie_country",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id")),
    Column("country_id", ForeignKey("countries.id")),
)

movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id")),
    Column("genre_id", ForeignKey("genres.id")),
)

movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id")),
    Column("actor_id", ForeignKey("actors.id")),
)


class Country(Base):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(Text, nullable=False)
    movies: Mapped[set['Movie']] = relationship('Movie', secondary=movie_country, back_populates='countries')

    def asdict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(Text, nullable=False)
    movies: Mapped[set['Movie']] = relationship('Movie', secondary=movie_genre, back_populates='genres')

    def asdict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Actor(Base):
    __tablename__ = "actors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(Text, nullable=False)
    movies: Mapped[set['Movie']] = relationship('Movie', secondary=movie_actor, back_populates='actors')

    def asdict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = Column(Integer, primary_key=True)
    created_at: Mapped[datetime] = Column(DateTime, server_default=func.now())
    name: Mapped[str] = Column(Text, nullable=False)
    description: Mapped[str] = Column(Text, nullable=False)
    premiere: Mapped[datetime] = Column(DateTime, nullable=True)
    director: Mapped[str] = Column(Text, nullable=False)
    countries: Mapped[set[Country]] = relationship('Country', secondary=movie_country, back_populates='movies')
    genres: Mapped[set[Genre]] = relationship('Genre', secondary=movie_genre, back_populates='movies')
    actors: Mapped[set[Actor]] = relationship('Actor', secondary=movie_actor, back_populates='movies')

    def asdict(self):
        result = {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        if self.countries:
            result['countries'] = [x.asdict() for x in self.countries]
        if self.genres:
            result['genres'] = [x.asdict() for x in self.genres]
        if self.actors:
            result['actors'] = [x.asdict() for x in self.actors]
        return result
