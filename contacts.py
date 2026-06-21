def add_contact(contacts):
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = number

def view_contact(contacts):
    name = input("Enter contact's name: ")
    for name in contacts:
        print(name, ":", contacts[name])

def delete_contact(contacts):
    name = input("Enter contact's name you want to delete: ")
    if name in contacts:
        contacts.pop(name)
    else:
        print("Contact doesn't exist!")

def search_contact(contacts):
    name = input("Enter contact's name: ")
    if name in contacts:
        print("Contact number : ", contacts[name])
    else :
        print("Contact doesn't exist!")

contacts = {}
print("Welcome to contacts")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    c = input("Enter your choice: ")
    if c == "1":
      add_contact(contacts)
    elif c == "2":
      view_contact(contacts)
    elif c == "3":
      search_contact(contacts)
    elif c == "4":
      delete_contact(contacts)
    elif c == "5":
      print("Goodbye!")
      break
