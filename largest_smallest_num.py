num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("Largest number is :" + str(num1))
elif num2 > num1 and num2 > num3:
    print("Largest number is :" + str(num2))
else :
    print("Largest number is :" + str(num3))

if num1 < num2 and num1 < num3:
    print("Smallest number is :" + str(num1))
elif num2 < num1 and num2 < num3:
    print("Smallest number is :" + str(num2))
else:
    print("Smallest number is :" + str(num3))
