def get_user_input():
    elements = []
    keys = set()  # To keep track of keys and check for duplicates
    while True:
        user_input = input("Enter an element in the format a1,0.1 (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            # Check if the input format is correct with one comma
            if user_input.count(",") != 1:
                raise ValueError("Invalid input format. Please enter in the format a1,0.1.")

            # Split the input by comma
            parts = user_input.split(",")

            # Check if the first part is non-empty (e.g., "a1")
            if not parts[0]:
                raise ValueError("Invalid input format. The key cannot be empty.")
            
            # Check for duplicate keys
            if parts[0] in keys:
                raise ValueError(f"Duplicate key detected: {parts[0]}")

            # Convert the second part to a float and check if it's in the range [0, 1]
            value = float(parts[1])
            if not 0 <= value <= 1:
                raise ValueError("The number must be in the range of 0 to 1. Please try again.")

            # Add to elements list and mark the key as used
            elements.append((parts[0], value))
            keys.add(parts[0])

        except ValueError as ve:
            print(ve)

    return elements

def calculate_support(elements):
    # Filter out elements with support value 0
    return [elem[1] for elem in elements if elem[1] > 0]

def calculate_core(elements):
    # Filter out elements with support value 0
    filtered_elements = [elem for elem in elements if elem[1] > 0]
    return max(filtered_elements, key=lambda x: x[1]) if filtered_elements else None

def calculate_normality(elements, total_support, threshold=0.5):
    return [(elem[0], 'Yes' if (elem[1] / total_support) > threshold else 'No') for elem in elements if elem[1] > 0]

def calculate_cardinality(elements):
    # Calculate the sum of supports and the number of elements with support > 0
    filtered_elements = [elem for elem in elements if elem[1] > 0]
    total_support = sum(elem[1] for elem in filtered_elements)
    count = len(filtered_elements)
    # Cardinality as the normalized value of support over number of elements
    return round(total_support / count, 2) if count > 0 else 0

# Example usage
elements_list = get_user_input()

if elements_list:
    # Calculate support
    support = calculate_support(elements_list)

    # Calculate core
    core = calculate_core(elements_list)

    # Calculate total support for normality calculation
    total_support = sum(support)

    # Calculate normality with a threshold
    normality = calculate_normality(elements_list, total_support)

    # Calculate cardinality as a normalized value
    cardinality = calculate_cardinality(elements_list)

    # Print results
    print("Elements List:", elements_list)
    print("Support:", support)
    print("Core Element:", core)
    print("Normality (Yes/No):", normality)
    print("Cardinality:", cardinality)
else:
    print("No elements were entered.")
