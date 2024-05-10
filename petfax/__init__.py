from flask import Flask
from . import pet
from . import fact

def create_app():
    app = Flask(__name__)
    
    # index route
    @app.route('/')
    def index(): 
        return 'Hello, this is PetFax!'

    #register Blueprints
    app.register_blueprint(pet.bp)  

    # register fact blueprint 
    app.register_blueprint(fact.bp)
    
    return app