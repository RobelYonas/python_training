def get_numbers():
    """
    Function to get numbers from user until 'done' is entered.
    Returns a list of integers.
    """
    numbers = []
    print("Enter the numbers you want to double, once done type 'done'")
    while True:
        user_input = input("Enter here: ")
        # Check if user has entered 'done'
        if user_input.lower() == "done":
            break
        numbers.append(int(user_input))

    return numbers


def double_numbers(numbers):
    """
    Function to double each number in the input list.
    Returns a new list.
    """
    # Apply lambda function to each number in the list
    return list(map(lambda x: x * 2, numbers))


# Get numbers from user
original_numbers = get_numbers()

# Double the numbers
doubled_numbers = double_numbers(original_numbers)

# Print the results
print("Original numbers:", original_numbers)
print("Doubled numbers:", doubled_numbers)
