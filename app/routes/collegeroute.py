from flask import *
from app.models.college import * 
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/college')
def College():
    colleges = college_list()
    return render_template('college.html', colleges=colleges)

@college_bp.route('/college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        new_college(collegecode, collegename)
        return redirect('/college') 
    return render_template('college.html')