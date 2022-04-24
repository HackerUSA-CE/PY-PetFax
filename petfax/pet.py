from flask import ( Blueprint, render_template ) 
import json
import jinja2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pets', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets='pets') 



