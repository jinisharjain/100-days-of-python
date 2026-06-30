students = {
    "Jinisha": {
        "Math": 95,
        "Science": 90,
        "English": 88
    },
    "Rahul": {
        "Math": 80,
        "Science": 76,
        "English": 85
    }
}

def add_student(students):
    s = input("Enter Student Name: ")
    if s in students:
        print("Student already exists")
    else:
        students[s] = {}
        students[s]["Math"] = int(input("Enter Math: "))
        students[s]["Science"] = int(input("Enter Science: "))
        students[s]["English"] = int(input("Enter English: "))
    return students

def view_student(students):
    print(students)

def search_student(students):
    s = input("Enter Student Name: ")
    if s in students:
        print(students[s])
        avg = sum(students[s].values()) / len(students[s])
        print("Average =", avg)
    else:
        print("Student does not exist")

def update_student(students):
    s = input("Enter Student Name: ")
    if s in students:
        sub = input("Enter Subject Name: ")
        if sub in students[s]:
            students[s][sub] = int(input("Enter Marks: "))
        else:
            print("Subject does not exist")
    else:
        print("Student does not exist")
    return students

def delete_student(students):
    s = input("Enter Student Name: ")
    if s in students:
        del students[s]
    else:
        print("Student does not exist")
    return students

def show_topper(students):
    topper = ""
    highest_avg = 0
    for name, subjects in students.items():
        avg = sum(subjects.values()) / len(subjects)
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    print("Topper : ", topper)

def class_average(students):
    avg = 0
    for s in students:
        avg += students[s]["Math"]
        avg += students[s]["Science"]
        avg += students[s]["English"]
    avg = avg / len(students)
    avg = avg/3
    print("Average = ", avg)

print("---Student Report Card---")
while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Show Class Average")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        students = add_student(students)
    elif choice == 2:
        view_student(students)
    elif choice == 3:
        search_student(students)
    elif choice == 4:
        students = update_student(students)
    elif choice == 5:
        students = delete_student(students)
    elif choice == 6:
        show_topper(students)
    elif choice == 7:
        class_average(students)
    elif choice == 8:
        print("Thank You")
        break
