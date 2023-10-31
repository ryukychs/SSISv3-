from flask import *
from app.models.course import * 
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/course')
def Course():
    courses = course_list()
    return render_template('course.html', courses=courses)

@course_bp.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        if check_course(coursecode):
            flash('Course Code already exists!', 'error')
        elif check_college(collegecode) != True:
            flash('College not found!', 'error')
        else:
            new_course(coursecode, coursename, collegecode)
            flash('Course added successfully!', 'success')
        return redirect('/course') 
    colleges = get_college_code()
    return render_template('addcourse.html', colleges=colleges)

@course_bp.route('/course/search', methods=['GET', 'POST'])
def search_courses():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('coursesearch')
        if search_query:
            courses = find_course(search_query)
    return render_template('course.html', courses=courses)

@course_bp.route('/course/delete/<string:coursecode>', methods=['DELETE'])
def remove_course(coursecode):
    if request.method == 'DELETE':
        del_course(coursecode)
        flash('Course deleted successfully!', 'success')
        return jsonify({'success': True})
    
@course_bp.route('/course/edit', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        college_code = request.form.get('college_code')
        update_course(course_code, course_name, college_code)
        flash('Course updated successfully!', 'success')
        return redirect('/course') 
    course_code = request.args.get('course_code')
    course_name = request.args.get('course_name')
    college_code = request.args.get('college_code')
    colleges = get_college_code()
    return render_template('editcourse.html', course_code=course_code, course_name=course_name, college_code=college_code, colleges=colleges)