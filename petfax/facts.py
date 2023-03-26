from flask import ( Blueprint, render_template )
import json

bp = Blueprint('facts', __name__, url_prefix='/facts')

@bp.route('/')
def index():
    return render_template('facts.html')

@bp.route('/new')
def new():
    return render_template('new_form.html')
