from flask_mysql_connector import MySQL

mysql = MySQL()

def student_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students
    