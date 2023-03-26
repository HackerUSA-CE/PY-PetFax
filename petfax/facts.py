from flask import ( Blueprint, render_template, request )
import json

bp = Blueprint('facts', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Thanks for submitting a fun fact!"
    return render_template('facts/index.html')

@bp.route('/new')
def new():
    return render_template('facts/new.html')
