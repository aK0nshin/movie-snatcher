from flask import Flask
from flask_elasticsearch import FlaskElasticsearch
from flask_sqlalchemy import SQLAlchemy

from config import config_manager

db_manager = SQLAlchemy()
es_manager = FlaskElasticsearch()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_manager[config_name])

    config_manager[config_name].init_app(app)

    db_manager.init_app(app)
    es_manager.init_app(app)

    with app.app_context():
        db_manager.create_all()

    from . import routes
    app.register_blueprint(routes.bp)

    return app
