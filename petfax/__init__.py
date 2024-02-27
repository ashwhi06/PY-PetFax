from flask import Flask
from . import pet

def create_app():
    app = Flask(__name__)
    
    # index route
    @app.route('/')
    def index(): 
        return 'Hello, this is PetFax!'

    #register Blueprints
    app.register_blueprint(pet.bp)  

    
    return app