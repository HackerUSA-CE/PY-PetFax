from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import main
    app.register_blueprint(main.bp)

    from . import pet
    app.register_blueprint(pet.bp)

    return app
