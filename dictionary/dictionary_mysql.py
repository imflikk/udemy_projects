#!/usr/bin/python3

import mysql.connector
import difflib

# Establish connection with remote MySQL database (minus credentials)
conn = mysql.connector.connect(
    user = '',
    password = '',
    host = '',
    database  = ''
)

cursor = conn.cursor()
results = []

def query_for_word(word):
    query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' % word)
    return cursor.fetchall()

def print_results(results):
    print("Definitions: ")
    count = 1

    for result in results:
        print(str(count) + ": " + result[1])
        count += 1


user_word = input("Enter a word: ")

words_query = cursor.execute('SELECT Expression FROM Dictionary WHERE Expression IS NOT NULL')
all_words = cursor.fetchall()
all_words_cleaned = []

for word in all_words:
    all_words_cleaned.append(word[0])

if user_word.lower() in all_words_cleaned:
    results = query_for_word(user_word)
elif user_word.title() in all_words_cleaned:
    results = query_for_word(user_word)
elif user_word.upper() in all_words_cleaned:
    results = query_for_word(user_word)
else:
    # Loop through results of close matches (top 3 by default) for the user's word in the JSON data
    # and prompt user if the similarity ratio is higher than 0.8
    for s in difflib.get_close_matches(user_word, all_words_cleaned):
        if difflib.SequenceMatcher(None, s, user_word).ratio() > 0.8:
            print("Did you mean '" + s + "'? (yes or no)")

            user_meant = input()

            # If user selects yes for suggested word, return the matching value
            if user_meant.lower() == "yes" or user_meant.lower() == 'y':
                results = query_for_word(s)
                break
                

        # If no words found with a high enough similarity ratio, return message that the 
        # user-submitted word wasn't found.
        else:
            print("Word not found.")
            exit(0)

if results:
    print_results(results)
else:
    print("Word not found.")

