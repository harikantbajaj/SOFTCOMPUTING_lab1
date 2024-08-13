set1 = set()
set2 = set()

set1_nums = int(input("Enter the number of elements in the first set: "))

for i in range(set1_nums):
    while True:
        a = int(input(f"Enter element {i + 1}: "))
        if a in set1:
            print("Duplicate element detected. Please enter a new element.")
        else:
            set1.add(a)
            break

set2_nums = int(input("Enter the number of elements in the second set: "))

if set2_nums <= 0:
    print("Error: The number of elements in the second set should be greater than zero.")
    exit()

for i in range(set2_nums):
    while True:
        a = int(input(f"Enter element {i + 1}: "))
        if a in set2:
            print("Duplicate element detected. Please enter a new element.")
        else:
            set2.add(a)
            break

print("The union of set 1 and set 2 is:", set1 | set2)
print("The intersection between set 1 and set 2 is:", set1 & set2)
print("The difference between set 1 and set 2 is:", set1 - set2)
