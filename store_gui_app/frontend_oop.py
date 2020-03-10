#!/usr/bin/python3

################
# **Object-Oriented Version**
#
# Front end, gui-related setup and functions for the "Book Store" app.  Anything related to the backend/database management is
# stored in database.py.
#
# Instructions to create executable version of the app:
#   - pip install pyinstaller
#   - pyinstaller --onefile --windowed frontend.py -n {name of output file}
#
################

from tkinter import *

# Import database.py script that contains functions for interacting with the database
from backend_oop import Database

# Create database object
database = Database()

selected_tuple = ()


class Window(object):

    # Create initial tkinter window object when gui is created
    def __init__(self, window):
        self.window = window

        # Assign title to Gui window
        self.window.wm_title("Book Store")

        # Create 4 labels for the entry fields
        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        # Create 4 entry fields and associated StringVar variables
        self.title_value = StringVar()
        self.e1 = Entry(window, textvariable=self.title_value)
        self.e1.grid(row=0, column=1)

        self.author_value = StringVar()
        self.e2 = Entry(window, textvariable=self.author_value)
        self.e2.grid(row=0, column=3)

        self.year_value = StringVar()
        self.e3 = Entry(window, textvariable=self.year_value)
        self.e3.grid(row=1, column=1)

        self.isbn_value = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        # Create listbox object to store the list of items retrieved from the database
        self.listbox1 = Listbox(window, height=6, width=35)
        self.listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Create bind event that will look for when an item is selected in the listbox and then run the get_selected_row function
        self.listbox1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Create scrollbar and attach to listbox
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        sb1.configure(command=self.listbox1.yview)
        self.listbox1.configure(yscrollcommand=sb1.set)



        # Create 6 buttons with various functions that will interact with the database
        but1 = Button(window, text="View all", width=12, command=self.view_command)
        but1.grid(row=2, column=3)

        but2 = Button(window, text="Search entry", width=12, command=self.search_command)
        but2.grid(row=3, column=3)

        but3 = Button(window, text="Add entry", width=12, command=self.add_command)
        but3.grid(row=4, column=3)

        but4 = Button(window, text="Update entry", width=12, command=self.update_command)
        but4.grid(row=5, column=3)

        but5 = Button(window, text="Delete entry", width=12, command=self.delete_command)
        but5.grid(row=6, column=3)

        but6 = Button(window, text="Close", width=12, command=self.window.destroy)
        but6.grid(row=7, column=3)

    # Function to look for "ListboxSelected" event, when a line is clicked on in the list box.
    # Fill in the entry fields with the contents of the line that is clicked on
    def get_selected_row(self, event):
        # Create global variable 'selected_tuple' that will contain the items in the clicked on line
        global selected_tuple

        # Try/except to prevent the program from crashing if the box is clicked on when the listbox is empty.
        try:
            index = self.listbox1.curselection()[0]
            selected_tuple = self.listbox1.get(index)

            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    # Empty the listbox, then use view_all function from backend to fill in every row currently in the database
    def view_command(self):
        self.listbox1.delete(0, END)
        for row in database.view_all():
            self.listbox1.insert(END, row)

    # Empty the listbox, then use the database.search function for any/all of the entry fields with information provided
    def search_command(self):
        self.listbox1.delete(0, END)

        for row in database.search(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()):
            self.listbox1.insert(END, row)

    # Use database.insert_item command to create a new row in the database table with the values currently in the entry fields, then refresh the listbox
    def add_command(self):
        database.insert_item(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.view_command()

    # Use database.delete to remove the row in the database containing the line currently selected in the listbox (selected_tuple[0]] is the id field in the database)
    def delete_command(self):
        database.delete_item(selected_tuple[0])
        self.view_command()

    # Use database.update_item function to get the row id of the listbox item currently selected, then update that row with the information in the entry fields
    def update_command(self):
        database.update_item(selected_tuple[0], self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.view_command()

# Initialize new tkinter window and instantiate it with a Window object
window = Tk()
Window(window)

# Start mainloop for GUI
window.mainloop()
