# This script prompts the user to enter a day of the week and then prints a message
# based on the input.

# Prompt the user to enter a day of the week and convert the input to lowercase
day_of_week = input("Enter a day of the week: ").lower()

# Check if the input is "tuesday" and print a message if it is
# The if statement checks if the day_of_week variable is equal to the string "tuesday"
# and if it is, it prints the message "Nice choice for Tuesday!"
if day_of_week == "tuesday":
    # Print a message indicating that Tuesday is a nice choice
    print('Nice choice for Tuesday!')

# Check if the input is "monday" and print a message if it is
# The elif statement checks if the day_of_week variable is equal to the string "monday"
# and if it is, it prints the message "It's going to be a long Monday."
elif day_of_week == "monday":
    # Print a message indicating that Monday is going to be a long day
    print("It's going to be a long Monday.")

# If the input is neither "tuesday" nor "monday", print a message indicating that the input is valid
# The else statement checks if the day_of_week variable is not equal to the string "tuesday" and "monday"
# and if it is, it prints the message indicating that the input is a valid day of the week.
else:
    # Print a message indicating that the input is a valid day of the week
    print(f"{day_of_week} is a valid day of the week.")


# Set of movie titles
movie_titles = {"Matrix", "Cars 2", "Cat vs Dog"}

# Prompt the user to enter a movie title and convert the input to title case
# The title method changes the first character of each word to uppercase
user_input = input("Enter the movie title you watched: ").title()

# Check if the user's input is in the set of movie titles
# The in keyword checks if a sequence (list, tuple, string, set) contains a value
if user_input in movie_titles:
    # Print a message indicating that the movie has been watched
    print(f"We have watched the movie {user_input}")
else:
    # Print a message indicating that the user's taste is quite unique
    print("Your taste is quite unique.")
    
