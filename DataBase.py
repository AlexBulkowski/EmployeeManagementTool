import mysql.connector
def get_connection_to_database():
    connection = mysql.connector.connect(
        user='root',
        password='Root123!',
        host='127.0.0.1',
        database='emp_database',
        auth_plugin='mysql_native_password')
    return connection
