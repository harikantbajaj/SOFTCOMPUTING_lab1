def fuzzy_union(mu_a, mu_b):
    return max(mu_a, mu_b)

def fuzzy_intersection(mu_a, mu_b):
    return min(mu_a, mu_b)

def fuzzy_complement(mu):
    return 1 - mu
def validate_fuzzy_set(fuzzy_set, name):
    if not fuzzy_set:
        raise ValueError(f"Error: Fuzzy sets {name} must not be empty.")
    elements = set()
    for element, membership_value in fuzzy_set:
        if membership_value < 0 or membership_value > 1:
            raise ValueError("Error: Membership values must be between 0 and 1.")
        if element in elements:
            raise ValueError(f"Error: Duplicate elements detected in the set {name}.")
        elements.add(element)
def get_fuzzy_set_input(name):
    n = int(input(f"Number of elements in set {name}: "))
    fuzzy_set = [(input(f"Element for {name}: "), float(input(f"Membership for {name}: "))) for _ in range(n)]
    validate_fuzzy_set(fuzzy_set, name)
    return fuzzy_set
try:
    A = get_fuzzy_set_input("A")
    B = get_fuzzy_set_input("B")

    union_result = [(a, fuzzy_union(mu_a, mu_b)) for (a, mu_a), (_, mu_b) in zip(A, B)]
    intersection_result = [(a, fuzzy_intersection(mu_a, mu_b)) for (a, mu_a), (_, mu_b) in zip(A, B)]
    complement_A = [(a, fuzzy_complement(mu_a)) for (a, mu_a) in A]
    complement_B = [(b, fuzzy_complement(mu_b)) for (b, mu_b) in B]

    print("\nUnion of A and B:", union_result)
    print("Intersection of A and B:", intersection_result)
    print("Complement of A:", complement_A)
    print("Complement of B:", complement_B)

except ValueError as e:
    print(e)
