from flask import Flask
from flask_bootstrap import Bootstrap


def create_app() -> Flask:
    flask_app = Flask(__name__)
    bootstrap = Bootstrap()
    bootstrap.init_app(flask_app)

    from app.main import bp as main_bp

    flask_app.register_blueprint(main_bp)

    return flask_app
