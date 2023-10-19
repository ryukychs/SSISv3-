from flask import *
from app.models.student import * 
from flask_wtf import *

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def Student():
    students = student_list()
    return render_template('student.html', students=students)

@student_bp.route('/student/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        new_student(id, firstname, lastname, coursecode, yearlevel, gender)
        return redirect('/student') 
    return render_template('student.html')

@student_bp.route('/student/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_student(search_query)
    return render_template('student.html', students=students)