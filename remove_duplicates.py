num = [4, 6, 8, 8, 20,20]
new = []
for num in num:
    if num not in new:
        new.append(num)
print(new)
