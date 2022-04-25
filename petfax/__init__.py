# config                    
from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    # from . import facts
    # app.register_blueprint(facts.bp)

    # return the app 
    return app

