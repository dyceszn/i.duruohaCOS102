import tkinter as tk
from tkinter import messagebox 

# Function for collecting users input

def getUsersInput():
    users_name = users_name_entry.get()
    users_location = users_location_entry.get()
    box_weight = int(box_weight_entry.get())
    messagebox.showinfo("Info", f"{users_name}, Your data has been collected successfully")
    calculatePrice(box_weight, users_location)


# Function for calculating the price

def calculatePrice(weight, location):
    if location == 'Ibeju-Lekki':
        if weight >= 10:
            price = 5000
            messagebox.showinfo("Price", f" Your price is {price}")
        else:
            price = 3500
            messagebox.showinfo("Price", f" Your price is {price}")
    elif location == 'Epe':
        if weight >= 10:
            price = 10000
            messagebox.showinfo("Price", f" Your price is {price}")
        else:
            price = 5000
            messagebox.showinfo("Price", f" Your price is {price}")
    else:
        messagebox.showinfo("error", f"Invalid Input! Please try again")
        return

# Handling button click event
def button_click():
    # Ask for user confirmation
    result = messagebox.askyesno("Confirmation", "Do you want to submit?")
    if result: # If true
        getUsersInput()


# Create main window
root = tk.Tk()
root.title("Simi Services")
root.geometry("300x200")

messagebox.showinfo("Welcome", "Welcome to Simi Services")

# Create entry fields for user input
users_name_label = tk.Label(root, text="Please enter name:")
users_name_label.pack()
users_name_entry = tk.Entry(root)  # Entry widget for name
users_name_entry.pack()

users_location_label = tk.Label(root, text="Please enter location:")
users_location_label.pack()
users_location_entry = tk.Entry(root)  # Entry widget for location
users_location_entry.pack()

box_weight_label = tk.Label(root, text="Please enter weight:")
box_weight_label.pack()
box_weight_entry = tk.Entry(root)  # Entry widget for weight
box_weight_entry.pack()

# Create a button to submit the data
submit_button = tk.Button(root, text="Submit", command=button_click)
submit_button.pack()

root.mainloop()
