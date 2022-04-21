import json
from flask import (Blueprint, render_template)

bp = Blueprint('pet', __name__, url_prefix="/pets")


pets = json.load(open('pets.json'))
# print(pets)


@bp.route('/')
def index():
    return render_template('./pets/index.html', pets=pets)
