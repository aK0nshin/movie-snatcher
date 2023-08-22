from flask import request

from app.services.movies import parse_movie_id_from_url, get_movie_info_by_id
from app.storage import get_movie_by_id, store_movie, find_movies, index_movie


def movie_add():
    film_url = request.json.get('film_url')
    if film_url is None:
        return "film_url is not provided in json", 400

    movie_id = parse_movie_id_from_url(film_url)
    if not movie_id:
        return f"film_url \"{film_url}\" is invalid, please provide a valid kinopoisk film url", 400

    movie_info = get_movie_info_by_id(movie_id)

    movie = get_movie_by_id(movie_id)
    if movie is not None:
        return movie.asdict()

    movie = store_movie(movie_id, movie_info)
    index_movie(movie)
    return movie.asdict()


def movie_search():
    search_query = request.json.get('search_query')
    movies = find_movies(search_query)

    return [movie.asdict() for movie in movies]
