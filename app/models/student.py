from flask_mysql_connector import MySQL

mysql = MySQL()

def student_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = """ SELECT students.*, CONCAT(colleges.collegename, ' (', courses.collegecode, ')') AS collegecode FROM students
    JOIN courses ON students.coursecode = courses.coursecode JOIN colleges ON courses.collegecode = colleges.collegecode"""
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def new_student(id, firstname, lastname, coursecode, yearlevel, gender, photo):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender, photo) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, firstname, lastname, coursecode, yearlevel, gender, photo))
    mysql.connection.commit()
    cursor.close()
   
    
def find_student(studentsearch):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + studentsearch + "%"
    cursor.execute("SELECT * FROM students WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students

def delete_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()

def update_student(id, firstname, lastname, coursecode, yearlevel, gender, photo):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s, photo = %s WHERE id = %s"
    cursor.execute(update_query, (firstname, lastname, coursecode, yearlevel, gender, photo, id))
    mysql.connection.commit()
    cursor.close()

def get_student_by_id(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    return student

def check_id(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def check_course(coursecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT coursecode FROM courses WHERE coursecode = %s", (coursecode,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    
def get_course_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM courses"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def read_student(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT students.id, students.firstname, students.lastname, students.yearlevel, students.gender, students.photo, courses.coursecode, courses.coursename, colleges.collegecode, colleges.collegename FROM students JOIN courses ON students.coursecode = courses.coursecode JOIN colleges ON courses.collegecode = colleges.collegecode WHERE students.id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result