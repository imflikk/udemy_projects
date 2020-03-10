#!/usr/bin/python3

################
# **Object-Oriented Version**
#
# Backend setup and functions for the "Book Store" app.  Everything related to interacting with the database is stored in this 
# file and the front-end setup is in frontend.py.
################

import sqlite3

# Class to contain methods for interacting with the database object
class Database:

    # Create database and/or table if it doesn't exist when program is launched and define the columns to be used
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

        self.conn.commit()

    # Function to insert an item into the database
    def insert_item(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))

        self.conn.commit()

    # Function to delete an item from the database based on its id
    def delete_item(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))

        self.conn.commit()  

    # Function to return everything currently in the 'book' table
    def view_all(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    # Function to return the rows from the 'book' table that match the contents of one or all of the entry fields
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()

        return rows

    # Update an item in the table with the information passed to it from the contents of the entry fields
    def update_item(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))

        self.conn.commit()

    # Close database connection when program is exited
    def __del__(self):
        self.conn.close()

