#!/usr/bin/python3

import json
import difflib

# Load data from JSON file into 'data' variable
data = json.load(open('data.json', 'r'))

# Create function to get user input and check against JSON data
def get_definition():
    user_word = input("Enter a word: ").lower()

    # If user-submitted word is a key in the JSON data, return the matching value
    if user_word in data.keys():
        return data[user_word]

    # If user-submitted word doesn't match a key in JSON data, check for similar words
    # and ask user if the most similar is the one they meant to type
    else:
        # Loop through results of close matches (top 3 by default) for the user's word in the JSON data
        # and prompt user if the similarity ratio is higher than 0.8
        for s in difflib.get_close_matches(user_word, data.keys()):
            if difflib.SequenceMatcher(None, s, user_word).ratio() > 0.7:
                print("Did you mean '" + s + "'? (yes or no)")

                user_meant = input()

                # If user selects yes for suggested word, return the matching value
                if user_meant.lower() == "yes":
                    return data[s]

        # If no words found with a high enough similarity ratio, return message that the 
        # user-submitted word wasn't found.
        return "Word not found."

# Call function and store resulting value in variable
definition = get_definition()

print("Definitions: ")
count = 1

# If the result is a list, then a correct word was returned and we should print each item in the list
# Else, print the string "Word not found."
if isinstance(definition, list):
    for s in definition:
        print(str(count) + ": " + s)
        count += 1
else:
    print(definition)


    