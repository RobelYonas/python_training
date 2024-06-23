# Creating a dictionary with initial key-value pairs
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Displaying the initial dictionary
print('Initial dictionary:', person)

# Accessing and printing a value using a key
print('Name:', person['name'])

# Adding a new key-value pair to the dictionary
person['profession'] = 'Engineer'
print('Dictionary after adding profession:', person)

# Updating an existing value in the dictionary
person['age'] = 31
print('Dictionary after updating age:', person)

# Removing a key-value pair from the dictionary using the pop method
removed_value = person.pop('city')
print('Removed value:', removed_value)
print('Dictionary after removing city:', person)

# Iterating through the dictionary and printing all key-value pairs
print('Iterating through dictionary:')
for key, value in person.items():
    print(f'{key}: {value}')

# Checking if a key exists in the dictionary
if 'name' in person:
    print('The key "name" exists in the dictionary')

# Getting a value with a default if the key does not exist
favorite_color = person.get('favorite_color', 'not specified')
print('Favorite color:', favorite_color)

# Clearing all items from the dictionary
person.clear()
print('Dictionary after clearing all items:', person)
