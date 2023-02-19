import mysql.connector
def get_connection_to_database():
    connection = mysql.connector.connect(
        user='root',
        password='Root123!',
        host='127.0.0.1',
        database='emp_database',
        auth_plugin='mysql_native_password')
    return connection

#Tables needed to run the program properly:

#Basic active employees table
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
  PRIMARY KEY (`EMPLOYEE_ID`)
)
"""

#Table for fired/resigned/retired employees
"""
CREATE TABLE `past_employees` (
  `EMPLOYEE_ID` INT NOT NULL,
  `FIRST_NAME` VARCHAR(45) NULL,
  `LAST_NAME` VARCHAR(45) NULL,
  `DEPARTMENT_ID` INT NULL,
  `HIRE_DATE` DATETIME NULL,
  `DEPARTURE_DATE` DATETIME NULL,
  `REASON_FOR_DEPARTURE` VARCHAR(45) NULL,
  PRIMARY KEY (`EMPLOYEE_ID`));
"""

#Table for tasks
"""
CREATE TABLE `tasks` (
  `TASK_ID` INT NOT NULL AUTO_INCREMENT,
  `EMPLOYEE_ID` INT NULL,
  `DEPARTMENT_ID` INT NULL,
  `TASK_TITLE` VARCHAR(45) NULL,
  `TASK_DESCRIPTION` VARCHAR(45) NULL,
  `PRORITY` INT NOT NULL,
  `EXPIRE_DATE` DATETIME NULL,
  PRIMARY KEY (`TASK_ID`));
"""