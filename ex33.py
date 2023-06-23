i = 0
numbers = []

while i < 23:
    print(f"at the top i is {i}")
    numbers.append(i)

    i = i + 2
    print("numbers now: ", numbers)
    print(f"at the bottom i is {i}")


print("the numbers: ")
for num in numbers:
    print (num)