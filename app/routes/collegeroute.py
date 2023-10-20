from flask import *
from app.models.college import * 
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/college')
def College():
    colleges = college_list()
    return render_template('college.html', colleges=colleges)

@college_bp.route('/college/add', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        new_college(collegecode, collegename)
        return redirect('/college') 
    return render_template('college.html')

@college_bp.route('/college/search', methods=['GET', 'POST'])
def search_colleges():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('collegesearch')
        if search_query:
            colleges = find_colleges(search_query)
    return render_template('college.html', colleges=colleges)

@college_bp.route('/colleges/delete/<string:collegecode>', methods=['DELETE'])
def remove_college(collegecode):
    if request.method == 'DELETE':
        print(collegecode)
        delete_college(collegecode)
        return jsonify({'success': True})
    
@college_bp.route('/edit_college', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        college_code = request.form.get('college_code')
        college_name = request.form.get('college_name')
        print(college_code, college_name)
        update_college(college_code, college_name)
        flash('College updated successfully!', 'success')
        return redirect('/college')
    college_code = request.args.get('college_code')
    college_name = request.args.get('college_name')
    return render_template('/college', college_code=college_code, college_name=college_name)
