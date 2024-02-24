from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new', methods=['POST'])
def new(): 
    print(request.form["name"])
    print(request.form["facts"])
    return redirect('/facts')


@bp.route('/')
def index(): 
    return render_template('facts/new.html')