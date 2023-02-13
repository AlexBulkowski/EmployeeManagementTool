import mysql.connector
import DataBase as db

#print out all employees from the database in the readable form -> function made to be called inside other functions
def display_employees():
    connection = db.get_connection_to_database()
    SelectSQL = "SELECT first_name, last_name, email, hire_date, salary FROM employees"
    cursor = connection.cursor()
    cursor.execute(SelectSQL)
    id = 1
    for(first_name, last_name, email, hire_date, salary) in cursor:
        print(f"Employee #{id}:\nName: {first_name.title()} {last_name.title()}\nE-mail: {email}\nEmployed since:{hire_date}\nEarns: {salary} per month")
        id += 1
    connection.close()

# Every employee has: employee_id, first_name, last_name, email,job_id,department_id, hire_date, salary
# Status (Active/Vacation/Sick_leave/Fired/Retired/Maternity_leave)
def add_employee():
    print("Creating a new employee")
    emp_first_name = str(input("Enter first name: ")).title()
    emp_last_name = str(input("Enter last name: ")).title()
    emp_email = f"{emp_first_name[0].lower()}.{emp_last_name.lower()}@company.com"
    #emp_job_id TO DO
    #emp_department_id -> depends on job_id
    emp_hire_date = str(input("Enter hire date in format yyyy-mmm-dd: "))
    emp_salary = int(input("Enter salary: "))

    connection = db.get_connection_to_database()
    cursor = connection.cursor()
    InsertSQL = "INSERT INTO employees(FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, SALARY, STATUS) " \
                "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(hire_date)s, %(salary)s, %(status)s)"
    InsertData={
        'first_name': emp_first_name,
        'last_name': emp_last_name,
        'email': emp_email,
        'job_id': emp_job_id,
        'department_id': emp_department_id,
        'hire_date': emp_hire_date,
        'salary': emp_salary,
        'status':'Active'
    }

    cursor.execute(InsertSQL, InsertData)
    connection.commit()
    print()
    print(f'New employee: {emp_first_name} {emp_last_name} has been added')

    connection.close()


