# Listening to Jigga by TARIQ ft Khaid

import csv
import tkinter as tk
from tkinter import messagebox 

# Function to load csv file and put it in an array

def load_csv(datapath): 
    dataset = []
    with open(datapath, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)
    return dataset

datapath = 'week-5/GIG-logistics.csv' 
datasheet = load_csv(datapath)
# print(datasheet)

# Function to check users validity and display others if valid

def checkUser(arr, lastname, firstname, department):
    found = False
    for elements in arr:
        if (elements[1:] == [lastname, firstname, department]):
            found = True
            break
    if (found == True):
        messagebox.showinfo("accept", f"Welcome {firstname}")
        displayOtherMembers(arr, department)
    else:
        messagebox.showinfo("reject", "Sorry, Employee does not exist.")

# Function to display other members

def displayOtherMembers(arr, department):
    membersArr = []
    for values in arr:
        if (values[3] == department):
            member = f"First name:{values[1]} Lastname:{values[2]} Department:{values[3]}\n"
            membersArr.append(member)
    messagebox.showinfo("members", membersArr)

# START POINT:
# GUI FOR COLLECTING USERS INPUT STARTS HERE
# OTHER FUNCTIONS ARE CALLED

# Handling button click event
def button_click():
    # Ask for user confirmation
    result = messagebox.askyesno("Confirmation", "Do you want to submit?")
    if result: # If true
        usersInput()

# Getting users input
def usersInput():
    lastName = lastName_entry.get() # Get users input and puts it in variable
    firstName = firstName_entry.get() 
    dept = dept_entry.get()
    messagebox.showinfo("Info", "Data collected successfully")
    messagebox.showinfo("Info", "Checking validity...")
    checkUser(datasheet, lastName, firstName, dept)

# Create main window
root = tk.Tk()
root.title("Validation Page")
root.geometry("300x200")

# Create entry fields for user input
lastName_label = tk.Label(root, text="Enter Last name:")
lastName_label.pack()
lastName_entry = tk.Entry(root)  # Entry widget for last name
lastName_entry.pack()

firstName_label = tk.Label(root, text="Enter First name:")
firstName_label.pack()
firstName_entry = tk.Entry(root)  # Entry widget for first name
firstName_entry.pack()

dept_label = tk.Label(root, text="Enter Department:")
dept_label.pack()
dept_entry = tk.Entry(root)  # Entry widget for department
dept_entry.pack()

# Create a button to submit the data
submit_button = tk.Button(root, text="Submit", command=button_click)
submit_button.pack()

root.mainloop()

# GUI FOR COLLECTING USERS INPUT ENDS HERE
