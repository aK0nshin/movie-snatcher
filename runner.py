import os

from dotenv import load_dotenv

from app import create_app, db_manager
from app.models import Movie, Country, movie_genre, movie_country, Genre, movie_actor, Actor

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv("FLASK_CONFIG") or "dev")


@app.shell_context_processor
def make_shell_context():
    return dict(db=db_manager, Movie=Movie, Country=Country, MovieCountry=movie_country, Genre=Genre,
                MovieGenre=movie_genre, Actor=Actor, MovieActor=movie_actor)
