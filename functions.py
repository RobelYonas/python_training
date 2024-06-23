# Defining a simple function that takes no arguments and returns no value
def greet():
    print("Hello, welcome to learning Python functions!")


# Calling the greet function
greet()


# Defining a function that takes one argument and prints a greeting
def greet_person(name):
    print(f"Hello, {name}! Welcome to learning Python functions!")


# Calling the greet_person function with an argument
greet_person('Alice')


# Defining a function that takes two arguments and returns a formatted string
def create_greeting(name, age):
    return f"Hello, {name}! You are {age} years old."


# Calling the create_greeting function and storing the result in a variable
greeting = create_greeting('Bob', 25)
# Printing the result
print(greeting)


# Defining a function that takes a list of numbers and returns their sum
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# Calling the sum_numbers function with a list of numbers and printing the result
numbers = [1, 2, 3, 4, 5]
total_sum = sum_numbers(numbers)
print(f"The sum of {numbers} is {total_sum}")


# Defining a function with default argument values
def introduce_person(name, age=30, city='New York'):
    print(f"This is {name}, they are {age} years old and live in {city}.")


# Calling the introduce_person function with different combinations of arguments
introduce_person('Charlie')
introduce_person('Dana', 22)
introduce_person('Eve', 28, 'San Francisco')


# Defining a function that demonstrates the use of keyword arguments
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


# Calling the display_info function using keyword arguments
display_info(age=40, city='Boston', name='Frank')


# Defining a function that takes variable-length arguments
def print_all(*args):
    for arg in args:
        print(arg)


# Calling the print_all function with multiple arguments
print_all('Python', 'is', 'fun')


# Defining a function that takes variable-length keyword arguments
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the print_key_values function with multiple keyword arguments
print_key_values(name='Grace', age=35, city='Seattle')
