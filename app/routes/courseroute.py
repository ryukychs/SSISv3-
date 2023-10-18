from flask import *
from app.models.course import * 
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/course')
def Course():
    courses = course_list()
    return render_template('course.html', courses=courses)

@course_bp.route('/course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        new_course(coursecode, coursename, collegecode)
        return redirect('/course') 
    return render_template('course.html')