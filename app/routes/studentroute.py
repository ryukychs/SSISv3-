from flask import *
from app.models.student import * 
from flask_wtf import *
import re

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def Student():
    students = student_list()
    return render_template('student.html', students=students)

@student_bp.route('/student/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        id = request.form['student-id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        if not re.match(r'^\d{4}-\d{4}$', id):
            flash('Invalid Student ID format. Follow YYYY-NNNN format.', 'error')
        elif check_id(id):
            flash('Student ID already exists!', 'error')
        elif check_course(coursecode) != True:
            flash('Course not found!', 'error')
        else:
            new_student(id, firstname, lastname, coursecode, yearlevel, gender)
            flash('Student added successfully!', 'success')
        return redirect('/student') 
    courses = get_course_codes()
    return render_template('addstudent.html', courses=courses)

@student_bp.route('/student/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_student(search_query)
    return render_template('student.html', students=students)

@student_bp.route('/students/delete/<string:id>', methods=['DELETE'])
def remove_college(id):
    if request.method == 'DELETE':
        delete_student(id)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})

@student_bp.route('/student/edit', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        gender = request.form.get('gender').capitalize()
        update_student(student_id, first_name, last_name, course_code, year_level, gender)
        flash('Student updated successfully!', 'success')
        return redirect('/student') 
    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    course_code = request.args.get('course_code')
    year_level = request.args.get('year_level')
    gender = request.args.get('gender')
    courses = get_course_codes()
    return render_template('editstudent.html', student_id=student_id, first_name=first_name, last_name=last_name, course_code=course_code, year_level=year_level, gender=gender, courses=courses)
