import DataBase
import Employees as e
from flask import Flask
from flask import jsonify
from flask import request

def logo():
    print()
    print("===============")
    print("EmployeeManagementTool by Alex Bulkowski")
    print("==============")
    print()
def show_main():
    logo()
    print("Please select an option:")
    print("1 - Add a new employee")
    print("2 - Delete an employee")
    print("3 - Edit an employee's data")
    print("4 - Assign a task to an employee")
    print("5 - Check employee's profile")
    print()
    print("6 - Summarize the company")
    print("7 - Show work schedule for the week")
    print("8 - Turn off")

def main():
    while True:
        show_main()
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice not in range(1,9):
                print("You can only put a number between 1 and 8")
            elif user_choice == 1:
                e.add_employee()
            elif user_choice == 2:
                print("you choose numer 2")
            elif user_choice == 3:
                print("you choose numer 3")
            elif user_choice == 4:
                print("you choose numer 4")
            elif user_choice == 5:
                print("you choose numer 5")
            elif user_choice == 6:
                print("you choose numer 6")
            elif user_choice == 7:
                print("you choose numer 7")
            elif user_choice == 8:
                print("you choose numer 8")
        except:
            print()
            print("SOMETHING WENT WRONG")
            print("You can only put a number between 1 and 8")

if __name__ == "__main__":
    main()

