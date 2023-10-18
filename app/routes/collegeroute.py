from flask import *
from app.models.college import * 
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/college')
def College():
    colleges = college_list()
    return render_template('college.html', colleges=colleges)