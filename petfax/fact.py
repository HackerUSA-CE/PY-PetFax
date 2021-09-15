from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def index(): 
    return render_template('facts/index.html')