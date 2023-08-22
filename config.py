import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_COOKIE_HTTPONLY = os.environ.get("SESSION_COOKIE_HTTPONLY")
    REMEMBER_COOKIE_HTTPONLY = os.environ.get("REMEMBER_COOKIE_HTTPONLY")
    SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE")
    ELASTICSEARCH_HOST = os.environ.get("ELASTICSEARCH_HOST")
    KINOPOISK_HOST = os.environ.get("KINOPOISK_HOST")
    KINOPOISK_TOKEN = os.environ.get("KINOPOISK_TOKEN")
    MOVIE_ID_PATTERN = os.environ.get("MOVIE_ID_PATTERN")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_RUN_HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")


class TestingConfig(Config):
    TESTING = True
    FLASK_RUN_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")


config_manager = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}
