#!/usr/bin/python3

################
# Front end, gui-related setup and functions for the "Book Store" app.  Anything related to the backend/database management is
# stored in backend.py.
#
# Instructions to create executable version of the app:
#   - pip install pyinstaller
#   - pyinstaller --onefile --windowed frontend.py -n {name of output file}
#
################

from tkinter import *

# Import backend.py script that contains functions for interacting with the database
import backend

# Function to look for "ListboxSelected" event, when a line is clicked on in the list box.
# Fill in the entry fields with the contents of the line that is clicked on
def get_selected_row(event):
    # Create global variable 'selected_tuple' that will contain the items in the clicked on line
    global selected_tuple

    # Try/except to prevent the program from crashing if the box is clicked on when the listbox is empty.
    try:
        index = listbox1.curselection()[0]
        selected_tuple = listbox1.get(index)

        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

# Empty the listbox, then use view_all function from backend to fill in every row currently in the database
def view_command():
    listbox1.delete(0, END)
    for row in backend.view_all():
        listbox1.insert(END, row)

# Empty the listbox, then use the backend.search function for any/all of the entry fields with information provided
def search_command():
    listbox1.delete(0, END)

    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        listbox1.insert(END, row)

# Use backend.insert_item command to create a new row in the database table with the values currently in the entry fields, then refresh the listbox
def add_command():
    backend.insert_item(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()

# Use backend.delete to remove the row in the database containing the line currently selected in the listbox (selected_tuple[0]] is the id field in the database)
def delete_command():
    backend.delete_item(selected_tuple[0])
    view_command()

# Use backend.update_item function to get the row id of the listbox item currently selected, then update that row with the information in the entry fields
def update_command():
    backend.update_item(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()


# Create tkinter window object and title
window = Tk()

window.wm_title("Book Store")

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
title_value = StringVar()
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0, column=1)

author_value = StringVar()
e2 = Entry(window, textvariable=author_value)
e2.grid(row=0, column=3)

year_value = StringVar()
e3 = Entry(window, textvariable=year_value)
e3.grid(row=1, column=1)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1, column=3)

# Create listbox object to store the list of items retrieved from the database
listbox1 = Listbox(window, height=6, width=35)
listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create bind event that will look for when an item is selected in the listbox and then run the get_selected_row function
listbox1.bind('<<ListboxSelect>>', get_selected_row)

# Create scrollbar and attach to listbox
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
sb1.configure(command=listbox1.yview)
listbox1.configure(yscrollcommand=sb1.set)



# Create 6 buttons with various functions that will interact with the database
but1 = Button(window, text="View all", width=12, command=view_command)
but1.grid(row=2, column=3)

but2 = Button(window, text="Search entry", width=12, command=search_command)
but2.grid(row=3, column=3)

but3 = Button(window, text="Add entry", width=12, command=add_command)
but3.grid(row=4, column=3)

but4 = Button(window, text="Update entry", width=12, command=update_command)
but4.grid(row=5, column=3)

but5 = Button(window, text="Delete entry", width=12, command=delete_command)
but5.grid(row=6, column=3)

but6 = Button(window, text="Close", width=12, command=window.destroy)
but6.grid(row=7, column=3)

# Start mainloop for GUI
window.mainloop()
