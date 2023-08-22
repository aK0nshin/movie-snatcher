from app import db_manager
from app.models import Movie, Country, Genre, Actor


def get_movie_by_id(movie_id: int) -> Movie | None:
    result = db_manager.session.execute(db_manager.select(Movie).filter_by(id=movie_id)).first()
    if not result:
        return None
    return result[0]


def store_movie(movie_id: int, movie_info: dict) -> Movie:
    movie = Movie(
        id=movie_id,
        name=movie_info['name'],
        description=movie_info.get('description'),
        premiere=movie_info.get('premiere', {}).get("russia"),
        director=[x['name'] for x in movie_info.get('persons') if x['enProfession'] == 'director'][0],
    )

    for film_country in movie_info['countries']:
        country = db_manager.session.execute(db_manager.select(Country).filter_by(name=film_country['name'])).first()
        if country is None:
            country = Country(name=film_country['name'])
            db_manager.session.add(country)
            db_manager.session.commit()
            db_manager.session.refresh(country)
        else:
            country = country[0]
        movie.countries.add(country)

    for film_genre in movie_info['genres']:
        genre = db_manager.session.execute(db_manager.select(Genre).filter_by(name=film_genre['name'])).first()
        if genre is None:
            genre = Genre(name=film_genre['name'])
            db_manager.session.add(genre)
            db_manager.session.commit()
            db_manager.session.refresh(genre)
        else:
            genre = genre[0]
        movie.genres.add(genre)

    for film_actor in movie_info['persons']:
        if film_actor['enProfession'] != 'actor':
            continue
        actor = db_manager.session.execute(db_manager.select(Actor).filter_by(id=film_actor['id'])).first()
        if actor is None:
            actor = Actor(
                id=film_actor['id'],
                name=film_actor['name']
            )
            db_manager.session.add(actor)
            db_manager.session.commit()
            db_manager.session.refresh(actor)
        else:
            actor = actor[0]
        movie.actors.add(actor)

    db_manager.session.add(movie)
    db_manager.session.commit()
    return movie
