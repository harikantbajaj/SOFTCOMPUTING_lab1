def fuzzy_union(mu_a, mu_b):
    return max(mu_a, mu_b)

def fuzzy_intersection(mu_a, mu_b):
    return min(mu_a, mu_b)

def fuzzy_complement(mu):
    return 1 - mu

def validate_fuzzy_set(fuzzy_set):
    if not fuzzy_set:
        raise ValueError("Error: Fuzzy sets must not be empty.")
    elements = set()
    for element, membership_value in fuzzy_set:
        if membership_value < 0 or membership_value > 1:
            raise ValueError("Error: Membership values must be between 0 and 1.")
        if element in elements:
            raise ValueError("Error: Duplicate elements detected in the set.")
        elements.add(element)

def get_fuzzy_set_input():
    n = int(input("Number of elements in set: "))
    fuzzy_set = [tuple(input(f"Element {i+1} and membership value: ").split()) for i in range(n)]
    fuzzy_set = [(element, float(membership_value)) for element, membership_value in fuzzy_set]
    validate_fuzzy_set(fuzzy_set)
    return fuzzy_set

def compute_de_morgan(A, B):
    # Calculate complements
    elements = set(a for a, _ in A).union(b for b, _ in B)
    complement_A = [(e, fuzzy_complement(next((mu_a for a, mu_a in A if a == e), 0))) for e in elements]
    complement_B = [(e, fuzzy_complement(next((mu_b for b, mu_b in B if b == e), 0))) for e in elements]
    
    # Calculate unions and intersections of complements
    union_complement = [(e, fuzzy_union(mu_a, mu_b)) for (e, mu_a), (_, mu_b) in zip(complement_A, complement_B)]
    intersection_complement = [(e, fuzzy_intersection(mu_a, mu_b)) for (e, mu_a), (_, mu_b) in zip(complement_A, complement_B)]
    
    # Calculate complements of intersections and unions
    A_intersection_B_complement = [(e, fuzzy_complement(fuzzy_intersection(next((mu_a for a, mu_a in A if a == e), 0),
                                                                      next((mu_b for b, mu_b in B if b == e), 0))))
                                   for e in elements]
    A_union_B_complement = [(e, fuzzy_complement(fuzzy_union(next((mu_a for a, mu_a in A if a == e), 0),
                                                              next((mu_b for b, mu_b in B if b == e), 0))))
                            for e in elements]
    
    return union_complement, A_intersection_B_complement, intersection_complement, A_union_B_complement

def main():
    print("Input for Set A:")
    A = get_fuzzy_set_input()
    print("Input for Set B:")
    B = get_fuzzy_set_input()

    try:
        # Compute results based on De-Morgan's Law
        union_complement, intersection_complement, intersection_result, union_result = compute_de_morgan(A, B)

        # Check if De-Morgan's laws are validated
        de_morgan_1 = all(
            abs(mu1 - mu2) < 1e-6 for (e1, mu1), (e2, mu2) in zip(union_complement, A_intersection_B_complement)
            if e1 == e2
        )
        de_morgan_2 = all(
            abs(mu1 - mu2) < 1e-6 for (e1, mu1), (e2, mu2) in zip(intersection_complement, A_union_B_complement)
            if e1 == e2
        )

        print("\nDe-Morgan's Law Validation:")
        print(f"A' ∪ B' = (A ∩ B)' : {'Valid' if de_morgan_1 else 'Invalid'}")
        print(f"A' ∩ B' = (A ∪ B)' : {'Valid' if de_morgan_2 else 'Invalid'}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
