import mysql.connector
def get_connection_to_database():
    connection = mysql.connector.connect(
        user='root',
        password='Root123!',
        host='127.0.0.1',
        database='emp_database',
        auth_plugin='mysql_native_password')
    return connection

#Table needed to run the program properly
"""
CREATE TABLE `employees` (
  `EMPLOYEE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` varchar(45) DEFAULT NULL,
  `LAST_NAME` varchar(45) DEFAULT NULL,
  `EMAIL` varchar(45) DEFAULT NULL,
  `DEPARTMENTS_ID` int(11) DEFAULT NULL,
  `JOB_ID` varchar(45) DEFAULT NULL,
  `HIRE_DATE` date DEFAULT NULL,
  `SALARY` int(11) DEFAULT NULL,
  `STATUS` varchar(45) DEFAULT 'Active',
  PRIMARY KEY (`EMPLOYEE_ID`)
)
"""