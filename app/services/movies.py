import re
import urllib

import requests
from flask import current_app


def parse_movie_id_from_url(film_url: str) -> int | None:
    app = current_app._get_current_object()
    parsed_url = re.search(app.config['MOVIE_ID_PATTERN'], film_url)
    if not parsed_url:
        return None
    movie_id = int(parsed_url.group(1))
    return movie_id


def get_movie_info_by_id(movie_id: int) -> dict:
    app = current_app._get_current_object()
    resp = requests.get(urllib.parse.urljoin(app.config['KINOPOISK_HOST'], f'/v1.3/movie/{movie_id}'),
                        headers={'X-API-KEY': app.config['KINOPOISK_TOKEN']})
    return resp.json()
