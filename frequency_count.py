dict1 = {}
n = int(input("Enter number of inputs: "))
num = []
for i in range(n):
    num.append(int(input("Enter number: ")))
for j in num:
    if j in dict1.keys():
        dict1[j] += 1
    else:
        dict1[j] = 1
print(dict1)
