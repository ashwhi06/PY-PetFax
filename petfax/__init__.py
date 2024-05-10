from flask import Flask
from . import pet
from . import fact
from . import models
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    # configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    # initialize database
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    # index route
    @app.route('/')
    def index(): 
        return 'Hello, this is PetFax!'

    #register Blueprints
    app.register_blueprint(pet.bp)  

    # register fact blueprint 
    app.register_blueprint(fact.bp)
    
    return app



   