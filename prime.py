def is_prime(n):
    count = 0
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
           count += 1
    if count == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_prime(num) == True:
    print("Prime")
else:
    print("Not prime")
