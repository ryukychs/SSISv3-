from flask_mysql_connector import MySQL

mysql = MySQL()

def college_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM colleges"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges
    
def new_college(collegecode, collegename):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO colleges (collegecode, collegename) VALUES (%s, %s)", (collegecode, collegename))
    mysql.connection.commit()
    cursor.close()
    
def find_colleges(collegesearch):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + collegesearch + "%"
    cursor.execute("SELECT * FROM colleges WHERE collegecode LIKE %s OR collegename LIKE %s", (search_query, search_query))   
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def delete_college(college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM colleges WHERE collegecode = %s", (college_code,))
    mysql.connection.commit()
    cursor.close()
    
def update_college(college_code, college_name):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE colleges SET collegename = %s WHERE collegecode = %s"
    cursor.execute(update_query, (college_name, college_code))
    mysql.connection.commit()
    cursor.close()
    
def check_college(collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT collegecode FROM colleges WHERE collegecode = %s", (collegecode,))
    result = cursor.fetchone()
    cursor.close()
    return result