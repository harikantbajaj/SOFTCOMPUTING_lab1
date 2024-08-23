def Input(a):
    l = set()
    for i in range(a):
        element = int(input("Enter the element: "))
        membership = float(input("Enter the membership: "))
        
        if membership < 0 or membership > 1:
            print("Error: Membership values must be between 0 and 1.")
            return None
        
        if any(e[0] == element for e in l):
            print("Error: Duplicate elements detected in the set.")
            return None
        
        l.add((element, membership))
    
    if not l:
        print("Error: Fuzzy sets must not be empty.")
        return None

    return l

def UnionFunc(setA, setB):
    unionSet = set()
    for i in setA:
        if i[0] in {e[0] for e in unionSet}:
            for j in unionSet:
                if j[0] == i[0]:
                    if j[1] < i[1]:
                        unionSet.remove(j)
                        unionSet.add(i)
                    break
        else:
            unionSet.add(i)
    
    for i in setB:
        if i[0] in {e[0] for e in unionSet}:
            for j in unionSet:
                if j[0] == i[0]:
                    if j[1] < i[1]:
                        unionSet.remove(j)
                        unionSet.add(i)
                    break
        else:
            unionSet.add(i)
    
    return unionSet

def Intersection(setA, setB):
    intersectionSet = set()
    for i in setA:
        if any(e[0] == i[0] for e in setB):
            intersectionSet.add(i)
    return intersectionSet

def Complement(setA, unionSet):
    complementSet = set()
    for i in unionSet:
        if i[0] not in {e[0] for e in setA}:
            complementSet.add(i)
    return complementSet

num1 = int(input("Size of the set A: "))
setA = Input(num1)
if setA is None:
    setA = set()

num2 = int(input("Size of the set B: "))
setB = Input(num2)
if setB is None:
    setB = set()

Union = UnionFunc(setA, setB)
print("Union: ", Union)
print("Intersection: ", Intersection(setA, setB))
print("Complement: ", Complement(setA, Union))