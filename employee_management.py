employees = {
    "Jinisha" : {
        "Age": 19,
        "Department": "AI & DS",
        "Salary": 50000
    },
    "Tanish" : {
        "Age": 20,
        "Department": "DS",
        "Salary": 50000
    }
}

def add_employee(employees):
    emp = input("Enter employee name : ")
    if emp in employees:
        print("Employee already exists")
    else:
        employees[emp] = {}
        employees[emp]["Age"] = input("Enter employee age : ")
        employees[emp]["Department"] = input("Enter Department : ")
        employees[emp]["Salary"] = input("Enter Salary : ")
        print("Employee added!")
    return employees

def view_employee(employees):
    for name, details in employees.items():
        print("--------------------")
        print("Name:", name)
        print("Age:", details["Age"])
        print("Department:", details["Department"])
        print("Salary:", details["Salary"])
        print("--------------------")

def search_employee(employees):
    emp = input("Enter employee name : ")
    if emp in employees.keys():
        print(employees[emp])
    else:
        print("Employee not found")

def update_salary(employees):
    emp = input("Enter employee name : ")
    if emp in employees:
        employees[emp]["Salary"] = input("Enter Salary : ")
        print("Salary updated successfully!")
    else:
        print("Employee not found")
    return employees

def delete_employee(employees):
    emp = input("Enter employee name : ")
    if emp in employees:
        del employees[emp]
        print("Employee deleted successfully!")
    else:
        print("Employee not found")
    return employees

print("---Employee Management---")
print("1. Add Employee")
print("2. View Employee")
print("3. Search Employee")
print("4. Update Salary")
print("5. Delete Employee")
print("6. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        employees = add_employee(employees)
    elif choice == 2:
        view_employee(employees)
    elif choice == 3:
        search_employee(employees)
    elif choice == 4:
        employees = update_salary(employees)
    elif choice == 5:
        employees = delete_employee(employees)
    elif choice == 6:
        print("Thank you for using this program")
        break
