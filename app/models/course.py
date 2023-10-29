from flask_mysql_connector import MySQL

mysql = MySQL()

def course_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def new_course(coursecode, coursename, collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO courses (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (coursecode, coursename, collegecode))
    mysql.connection.commit()
    cursor.close()
    
def find_course(coursesearch):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + coursesearch + "%"
    cursor.execute("SELECT * FROM courses WHERE coursecode LIKE %s OR coursename LIKE %s OR collegecode LIKE %s", (search_query, search_query, search_query))   
    courses = cursor.fetchall()
    cursor.close()
    return courses

def del_course(coursecode):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM courses WHERE coursecode = %s", (coursecode,))
    mysql.connection.commit()
    cursor.close()
    
def update_course(coursename, coursecode, collegecode):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE courses SET coursename = %s, collegecode = %s WHERE coursecode = %s"
    cursor.execute(update_query, (coursename, collegecode, coursecode))
    mysql.connection.commit()
    cursor.close()
    
def get_course_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM courses"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def get_college_code():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM colleges"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def check_course(coursecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT coursecode FROM courses WHERE coursecode = %s", (coursecode,))
    result = cursor.fetchone()
    cursor.close()
    return result

def check_college(collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT collegecode FROM colleges WHERE collegecode = %s", (collegecode,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True