import mysql.connector
import DataBase as db

#print out all employees from the database in the readable form -> function made to be called inside other functions
def display_employees():
    connection = db.get_connection_to_database()
    SelectSQL = "SELECT employee_id,first_name, last_name, email, hire_date, salary FROM employees"
    cursor = connection.cursor()
    cursor.execute(SelectSQL)

    for(employee_id,first_name, last_name, email, hire_date, salary) in cursor:
        print(f"Employee ID {employee_id}:\nName: {first_name.title()} {last_name.title()}\nE-mail: {email}\nEmployed since:{hire_date}\nEarns: {salary} per month")

    connection.close()

# Every employee has: employee_id, first_name, last_name, email,job_id,department_id, hire_date, salary
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
    InsertSQL = "INSERT INTO employees(FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, SALARY) " \
                "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(hire_date)s, %(salary)s"
    DataQuery={
        'first_name': emp_first_name,
        'last_name': emp_last_name,
        'email': emp_email,
        'job_id': emp_job_id,
        'department_id': emp_department_id,
        'hire_date': emp_hire_date,
        'salary': emp_salary
    }

    cursor.execute(InsertSQL, DataQuery)
    connection.commit()
    print()
    print(f'New employee: {emp_first_name} {emp_last_name} has been added')

    connection.close()

# Editing every variable employees have
def edit_employee():
    print("=== Edit Employee's profile ===")
    print()
    display_employees()
    print()
    print("Edit Employee's profile")
    user_choice = int(input("Enter employee's ID: "))
    print("What do you want to edit:")
    print()
    print("1 - First name")
    print("2 - Last name")
    print("3 - Job ID")
    print("4 - Hire date")
    print("5 - Salary")
    user_choice2 = int(input("Enter your choice: "))

    try:
        if user_choice2 not in range(1,6):
            print("You can only put a number between 1 and 5")
            print("Try again!")
        elif user_choice2 == 1:
            user_choice2 = "FIRST_NAME"
        elif user_choice2 == 2:
            user_choice2 = "LAST_NAME"
        elif user_choice2 == 3:
            user_choice2 = "JOB_ID"
        elif user_choice2 == 4:
            user_choice2 = "HIRE_DATE"
        elif user_choice2 == 5:
            user_choice2 = "SALARY"
    except:
        print("Something went worng!")
        print("Try again")

    connection = db.get_connection_to_database()
    cursor = connection.cursor()

    SelectSQL = f'SELECT {user_choice2} FROM employees WHERE employee_id= %(user_choice)s'

    cursor.execute(SelectSQL)
    for data in cursor:
        data = data[0]

    print(f"The current value you want to change is: {data}")
    user_choice3 = input("Enter the value you want to change to: ")

    UpdateSQL = f"UPDATE employees SET {user_choice2} = %(user_choice3)s WHERE employee_id= %(user_choice)s"
    DataQuery={
            'user_choice3': user_choice3,
            'user_choice': user_choice
    }
    cursor.execute(UpdateSQL, DataQuery)
    connection.commit()
    connection.close()
    print(f"You have successfully edited employee's number: {user_choice} profile!")

def remove_employee():
    print("=== Remove Employee's profile ===")
    print()
    display_employees()
    print("Remove Employee's profile")
    user_choice_id = int(input("Enter employee's ID: "))
    print()
    print("What is the reason for removing an employee?")
    print("1 - Fired by company")
    print("2 - Dismissal by employee")
    print("3 - Retirement")
    print("4 - Other")
    user_choice_reason = int(input("Enter number 1-4: "))
    try:
        if user_choice_reason not in range(1,5):
            print("You can only put a number between 1 and 4")
            print("Try again!")
        elif user_choice_reason == 1:
            user_choice_reason = "Fired by company"
        elif user_choice_reason == 2:
            user_choice_reason = "Dismissal by employee"
        elif user_choice_reason == 3:
            user_choice_reason = "Retirement"
        elif user_choice_reason == 4:
            user_choice_reason = "Other"
        else:
            user_choice_reason = "Other"
    except:
        print("Something went worng!")
        print("Try again")
    departure_date = input("Enter departure date in format yyyy-mmm-dd: ")

    connection = db.get_connection_to_database()
    cursor = connection.cursor()

    SelectSQL = f"SELECT employee_id, first_name, last_name, department_id, hire_date  FROM employees WHERE EMPLOYEE_id = {str(user_choice_id)}"
    cursor.execute(SelectSQL)
    for(employee_id, first_name, last_name, department_id, hire_date) in cursor:
        emp_data={
            "employee_id": employee_id,
            "first_name": first_name,
            "last_name": last_name,
            "department_id": department_id,
            "hire_date": hire_date,
        }
    emp_data["departure_date"] = departure_date
    emp_data["reason_for_departure"] = user_choice_reason

    InsertSQL = "INSERT INTO past_employees(EMPLOYEE_ID,FIRST_NAME, LAST_NAME, DEPARTMENT_ID, HIRE_DATE, DEPARTURE_DATE, REASON_FOR_DEPARTURE) " \
                "VALUES(%(employee_id)s,%(first_name)s, %(last_name)s, %(department_id)s, %(hire_date)s, %(departure_date)s, %(reason_for_departure)s)"
    DeleteSQL = f"DELETE FROM employees WHERE EMPLOYEE_ID = {str(user_choice_id)}"

    cursor.execute(InsertSQL, emp_data)
    connection.commit()
    cursor.execute(DeleteSQL)
    connection.commit()
    connection.close()

    print(f"You have successfully removed employee's number: {user_choice_id} profile!" )