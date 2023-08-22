# Standard Library imports

# Core Flask imports
from flask import Blueprint

# Third-party imports

# App imports
from app import db_manager
from .views import movies_views

bp = Blueprint('routes', __name__)

# alias
db = db_manager.session


# Request management
@bp.before_app_request
def before_request():
    db()


@bp.teardown_app_request
def shutdown_session(response_or_exc):
    db.remove()


# Public API
bp.add_url_rule(
   "/api/v1/movies", view_func=movies_views.movie_add, methods=["POST"]
)

bp.add_url_rule(
   "/api/v1/movies/search", view_func=movies_views.movie_search, methods=["POST"]
)
