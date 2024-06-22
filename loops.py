import random

# The user can choose to play or not by entering 'Y' or 'n' respectively.
# If the user chooses to play, the program generates a random number and prompts the user to guess it.
# The user has unlimited chances to guess the correct number.

# --------------------
# While loops
# --------------------

while True:
    # Prompt the user to play the game or quit
    user_input = input("Do you want to play the game (Y/n)? ")

    # If the user chooses to quit, break out of the loop
    if user_input.lower() == "n":
        break

    # Generate a random number between 0 and 9
    number = random.randint(0, 9)

    # Prompt the user to guess the number until they get it correct
    while True:
        guess = int(input("Guess a number: "))

        # Check if the guess is correct
        if guess == number:
            # If correct, print a message and break out of the loop
            print("Correct guess!")
            break
        else:
            # If incorrect, print a message and prompt the user to guess again
            print("Wrong guess, try again.")


# Asks the user to enter their name and the number of times to repeat it
users_name = input("Enter your name: ")  # Prompts the user to enter their name
repeating_Number = int(input("How many times to repeat your name: "))  # Prompts the user to enter the number of times to repeat their name

# Uses a for loop to repeat the name the specified number of times
# The range function generates a sequence of numbers from 0 to the number of times to repeat
# The f-string is used to format the output with the user's name
for i in range(repeating_Number):
    print(f"{users_name}")  # Prints the user's name the specified number of times


# A list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Create a new list by multiplying each number in the original list by 2
# Using a list comprehension
#
# The list comprehension syntax is as follows:
# [expression for item in iterable]
# Where expression is the operation to be applied to each item
# iterable is the list of items to iterate over
# Here, the operation is multiplying each item by 2
# And the iterable is the list of numbers

# The resulting list is assigned to the variable double_numbers
# Each item in the list of numbers is multiplied by 2, and the result is stored in a new list
double_numbers = [x * 2 for x in numbers]

# Print the double_numbers list
# This will print the list of numbers in the original list, multiplied by 2
print(double_numbers)

# Print the id of the original list and the new list
# The id function returns a unique identifier for the object, which in this case is the memory address of the list
# This is useful for debugging and understanding how the list is stored in memory
print("numbers: ", id(numbers), "doubles: ", id(double_numbers))
