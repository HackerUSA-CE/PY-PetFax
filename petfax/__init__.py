from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__, static_url_path='/static',static_folder='static')

    #Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mireyda2005!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    @app.route('/')
    def index(): 
        return 'Hello, PetFax!' 
    
    from . import pet 
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app