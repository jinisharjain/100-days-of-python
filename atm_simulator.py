def check_balance(balance):
    print("Your balance is: ", balance)

def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("₹", amount, "withdrawn successfully!")
    return balance

def deposit(balance):
    w = int(input("Enter amount to deposit: "))
    if w<=0:
        print("You can't deposit negative amount")
    else:
        balance = balance + w
        print("Amount deposited successfully")
    return balance


balance = 1000
print("---ATM---")

while True:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    c = input("Enter your choice: ")
    if c == "1":
      check_balance(balance)
    elif c == "2":
      balance = withdraw(balance)
    elif c == "3":
      balance = deposit(balance)
    elif c == "4":
      print("Goodbye!")
      break
