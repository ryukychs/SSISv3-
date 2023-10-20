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
        new_course(coursecode, coursename, collegecode)
        return redirect('/course') 
    return render_template('course.html')

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
        print(coursecode)
        del_course(coursecode)
        return jsonify({'success': True})
    
@course_bp.route('/edit_course', methods=['POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('coursecode')
        course_name = request.form.get('coursename')
        college_code = request.form.get('collegecode')
        print(course_code, course_name)
        update_course(course_name, course_code)
        flash('course updated successfully!', 'success')
        return redirect('/course')
    course_code = request.args.get('coursecode')
    course_name = request.args.get('coursename')
    college_code = request.args.get('collegecode')
    return render_template('/course')
