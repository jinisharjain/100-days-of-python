def add_student(num):
    dict1 = {}
    for i in range (num):
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        dict1[name] = marks
    print("Student records: ")
    print(dict1)
    avg = sum(dict1.values())/len(dict1)
    print("Average marks: " + str(avg))
    max_marks = list(dict1.values())[0]
    max_names = list(dict1.keys())[0]
    for name, marks in dict1.items():
        if marks > max_marks:
            max_marks = marks
            max_names = name
    print("Maximum marks: " + str(max_marks))
    print("Maximum scorer: " + str(max_names))

num = int(input("Enter number of students: "))
add_student(num)
