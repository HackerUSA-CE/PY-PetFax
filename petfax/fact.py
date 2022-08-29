from flask import ( Blueprint, render_template,request,redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new',methods=['GET','POST'])
def new(): 
    print(request.form)
    return render_template('facts/new.html')

@bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    
    return "thank you for submitting"