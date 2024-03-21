from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!' 
    
    from . import pet 
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app