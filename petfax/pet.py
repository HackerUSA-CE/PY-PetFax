from flask import ( Blueprint, render_template ) 
import json


pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pets', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets='pets') 



