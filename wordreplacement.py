# Prompt the user to enter the initial sentence and store it in a variable
sentence = input('Please enter the initial sentence: ')

# Display the sentence back to the user for confirmation
print('Your entered sentence: ' + sentence)

# Prompt the user to enter the word they want to replace in the sentence
wordToReplace = input('Please enter the word you want to replace: ')

# Prompt the user to enter the replacement word
replacementWord = input('Please enter the replacement word: ')

# Perform the replacement operation and store the result in a new variable
modified_sentence = sentence.replace(wordToReplace, replacementWord)

# Display the modified sentence to the user
print('The modified sentence is: ' + modified_sentence)
