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