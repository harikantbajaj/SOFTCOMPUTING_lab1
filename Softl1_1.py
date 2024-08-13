uni = set()
set1 = set()
set2 = set()

uni_nums = int(input("Enter the number of elements in the union set: "))

for i in range(uni_nums):
    a = int(input("Enter element {i}: "))
    if(a in uni):
        print("element present in the universal set")
        a = int(input("Enter new element "))
    uni.add(a)

set1_nums = int(input("Enter the number of elements in the first set: "))
if(set1_nums == 0):
    print("The set cannot be empty")
    exit()

for i in range(set1_nums):
    a = int(input("Enter element {i}: "))
    if(a not in uni):
        print("Not available in the universal set")
        a = int(input("Enter a new element: "))
    if(a in set1):
        print("element present in the  set")
        a = int(input("Enter new element "))
    set1.add(a)



set2_nums = int(input("Enter the number of elements in the second set: "))
if(set2_nums == 0):
    print("The set cannot be empty")
    exit()
for i in range(set2_nums):
    a = int(input("Enter element {i}: "))
    if(a not in uni):
        print("Not available in the universal set")
        a = int(input("Enter a new element: "))
    if(a in set2):
        print("element present in the  set")
        a = int(input("Enter new element "))
    set2.add(a)

print("The complement of set 1 is:", uni-set1)
print("The complement of set 2 is:", uni-set2)

for x in set1:
    for y in set2:
        if(x in uni and y in uni):
            print("[",x,y,"]")
        else:
            print("Element is not present in universal set")
            exit()
            
            
            
