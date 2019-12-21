#!/usr/bin/python3

################
# Backend setup and functions for the "Book Store" app.  Everything related to interacting with the database is stored in this 
# file and the front-end setup is in frontend.py.
################

import sqlite3

# Create database and/or table if it doesn't exist when program is launched and define the columns to be used
def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

    conn.commit()
    conn.close()

# Function to insert an item into the database
def insert_item(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))

    conn.commit()
    conn.close()

# Function to delete an item from the database based on its id
def delete_item(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM book WHERE id=?", (id,))

    conn.commit()
    conn.close()     

# Function to return everything currently in the 'book' table
def view_all():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()

    conn.close()

    return rows

# Function to return the rows from the 'book' table that match the contents of one or all of the entry fields
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()

    conn.close()

    return rows

# Update an item in the table with the information passed to it from the contents of the entry fields
def update_item(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))

    conn.commit()
    conn.close() 


connect()