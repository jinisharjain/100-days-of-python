books = {
    "Harry Potter": "Available",
    "Atomic Habits": "Available",
    "Python Crash Course": "Available",
    "The Alchemist": "Available"
}

def borrow_book(book):
    b = input("Enter the book you want to borrow")
    if b in books:
        if books[b] == "Available":
            print("Book borrowed")
            books[b] = "Borrowed"
        elif books[b] == "Borrowed":
            print("Book not available")
    else:
        print("Book not available in library")

def return_book(book):
    b = input("Enter the book you want to return")
    if b in books:
        if books[b] == "Borrowed":
            print("Book returned")
            books[b] = "Available"
    else:
        print("Book not available in library")

def add_book(book):
    b = input("Enter the book you want to add")
    if b in books:
        print("Book already exists")
    else:
        books[b] = ("Available")
        print("Book added")

print("---Library---")
print("1. View Books")
print("2. Borrow Book")
print("3. Return Book")
print("4. Add Book")
print("5. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(books)
    elif choice == 2:
        books = borrow_book(books)
    elif choice == 3:
        books = return_book(books)
    elif choice == 4:
        books = add_book(books)
    elif choice == 5:
        print("Thank you for using this program")
        break
