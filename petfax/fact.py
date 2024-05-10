from flask import ( Blueprint, redirect, render_template, request ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')