expenses = {
    "Food": {
        "Pizza": 350,
        "Burger": 200
    },
    "Travel": {
        "Bus": 100,
        "Cab": 450
    }
}

def add_expense(expenses):
    category = input("Enter category: ")
    if category in expenses:
        expense = input("Enter expense name: ")
        amount = int(input("Enter amount: ₹"))
        if expense in expenses[category]:
            expenses[category][expense] += amount
        else:
            expenses[category][expense] = amount
        print("Expense added successfully!")
    else:
        print("Category not found!")
    return expenses


def view_expenses(expenses):
    print("\n------ Expenses ------")
    for category, items in expenses.items():
        print(f"\nCategory : {category}")
        for expense, amount in items.items():
            print(f"{expense} : ₹{amount}")


def search_category(expenses):
    category = input("Enter category: ")
    if category in expenses:
        print(f"\nCategory : {category}")
        for expense, amount in expenses[category].items():
            print(f"{expense} : ₹{amount}")
    else:
        print("Category not found!")


def delete_expense(expenses):
    category = input("Enter category: ")
    if category in expenses:
        expense = input("Enter expense name: ")
        if expense in expenses[category]:
            del expenses[category][expense]
            print("Expense deleted successfully!")
            if len(expenses[category]) == 0:
                del expenses[category]
        else:
            print("Expense not found!")
    else:
        print("Category not found!")
    return expenses

def total_expenses(expenses):
    grand_total = 0
    print("\n------ Expense Summary ------")
    for category, items in expenses.items():
        category_total = 0
        for amount in items.values():
            category_total += amount
        print(f"{category} : ₹{category_total}")
        grand_total += category_total

    print("----------------------------")
    print(f"Total Expense : ₹{grand_total}")

print("\n====== Expense Tracker ======")
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Category")
    print("4. Delete Expense")
    print("5. Total Expenses")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        expenses = add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        search_category(expenses)
    elif choice == "4":
        expenses = delete_expense(expenses)
    elif choice == "5":
        total_expenses(expenses)
    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice!")
