# Define sets of family members
family_members_inside = {'mom', 'dad', 'brother', 'sister'}
family_members_outside = {'dad', 'mom'}

# Print out the names of family members who are outside
# The difference operation returns a new set with elements from the first set 
# that are not in the second set
# The docstring for the difference method:
# "Return a new set with elements in the set that are not in others"
print(family_members_outside.difference(family_members_inside))


# Define sets of Swedish and Danish friends
swedish_friends = {'carl', 'bob', 'Jonas'}
danish_friends = {'Alex', 'Peter', 'Olle'}

# Print out the set of all unique friends
# The union operation returns a new set with all elements from both sets
# The docstring for the union method:
# "Return a new set with elements from the set and all others"
print(swedish_friends.union(danish_friends))  # Output: {'Olle', 'Alex', 'bob', 'Jonas', 'Peter', 'carl'}

# Define sets of JavaScript and Python programmers
javascript_programmer = {'Robert', 'Noah'}
python_programmer = {'Brain', 'Robert'}

# Print out the set of all programmers who are proficient in both languages
# The intersection operation returns a new set with elements common to both sets
# The docstring for the intersection method:
# "Return a new set with elements common to the set and all others"
print(javascript_programmer.intersection(python_programmer))


# Check if the two sets are the same object in memory
# Returns True if they are the same object, False otherwise
# The is operator checks if two objects are the same object in memory
print(danish_friends is swedish_friends)  # Output: False. The two sets are different objects in memory
