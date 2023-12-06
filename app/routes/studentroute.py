from flask import *
from app.models.student import * 
from flask_wtf import *
import re
from config import CLOUDINARY_FOLDER
import cloudinary
from cloudinary.uploader import upload as cloudinary_upload
from cloudinary.utils import cloudinary_url
student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def student():
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
        photo = request.form['photo']
        if not re.match(r'^\d{4}-\d{4}$', id):
            flash('Invalid Student ID format. Follow YYYY-NNNN format.', 'error')
        elif check_id(id):
            flash('Student ID already exists!', 'error')
        elif check_course(coursecode) != True:
            flash('Course not found!', 'error')
        else:
            new_student(id, firstname, lastname, coursecode, yearlevel, gender, photo)
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
def remove_student(id):  # Corrected function name and parameter
    if request.method == 'DELETE':
        delete_student(id)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})

@student_bp.route('/student/edit', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        photo = request.form.get('photo')
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        gender = request.form.get('gender').capitalize()
        update_student(student_id, first_name, last_name, course_code, year_level, gender, photo)
        flash('Student updated successfully!', 'success')
        return redirect('/student') 
    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    course_code = request.args.get('course_code')
    year_level = request.args.get('year_level')
    gender = request.args.get('gender')
    photo = request.args.get('photo')
    courses = get_course_codes()
    return render_template('editstudent.html', student_id=student_id, first_name=first_name, last_name=last_name, course_code=course_code, year_level=year_level, gender=gender, courses=courses, photo=photo)


@student_bp.route('/upload/cloudinary/', methods=['POST'])
def upload_to_cloudinary():
    file = request.files.get('file')

    if file:
        upload_result = cloudinary_upload(
            file, folder=CLOUDINARY_FOLDER)

        return jsonify({
            'is_success': True,
            'url': upload_result['secure_url']
        })

    return jsonify({
        'is_success': False,
        'error': 'Missing file'
    })