from flask import *
from app.models.student import * 
from flask_wtf import *

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def Student():
    students = student_list()
    return render_template('student.html', students=students)