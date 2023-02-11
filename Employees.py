import mysql.connector
import DataBase as db

# Every employee has: employee_id, first_name, last_name, email, hire_date, salary
def add_employee():
    print("Creating a new employee")
    emp_first_name = str(input("Enter first name: ")).title()
    emp_last_name = str(input("Enter last name: ")).title()
    emp_email = f"{emp_first_name[0].lower()}.{emp_last_name.lower()}@company.com"
    emp_hire_date = str(input("Enter hire date in format yyyy-mmm-dd: "))
    emp_salary = int(input("Enter salary: "))

    connection = db.get_connection_to_database()
    cursor = connection.cursor()
    InsertSQL = "INSERT INTO employees(FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, SALARY) " \
                "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(hire_date)s, %(salary)s)"
    InsertData={
        'first_name': emp_first_name,
        'last_name': emp_last_name,
        'email': emp_email,
        'hire_date': emp_hire_date,
        'salary': emp_salary}

    cursor.execute(InsertSQL, InsertData)
    connection.commit()
    print()
    print(f'New employee: {emp_first_name} {emp_last_name} has been added')

    connection.close()


