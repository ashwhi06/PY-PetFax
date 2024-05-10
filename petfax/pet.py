from flask import (Blueprint, render_template)
import json

bp = Blueprint(
    "pet", 
    __name__,
     url_prefix="/pets"
)

@bp.route("/")
def pets():
    pets = json.load(open('pets.json'))
    return render_template('pets/index.html', title="This is PetFax", pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pets = json.load(open('pets.json'))
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)