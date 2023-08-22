import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app("test")
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


def test_movie_snatch(client):
    response = client.post("/api/v1/movies", json={
      "film_url": "https://www.kinopoisk.ru/film/435"
    })
    assert response.status_code == 200


def test_movie_search(client):
    response = client.post("/api/v1/movies/search", json={
      "search_query": "Хэнкс"
    })
    assert response.status_code == 200
