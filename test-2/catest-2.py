import tkinter as tk
from tkinter import messagebox

# Dictionary

rice_and_pasta = {
    1: {"name": "Jollot Rice", "price": 350},
    2: {"name": "Coconut Fried Rice", "price": 350},
    3: {"name": "Jollof Spaghetti", "price": 350},
}
proteins = {
    1: {"name": "Sweet Chilli Chicken", "price": 1100},
    2: {"name": "Grilled Chicken Wings", "price": 400},
    3: {"name": "Fried Beef", "price": 400},
    4: {"name": "Fried Fish", "price": 500},
    5: {"name": "Boiled Eggs", "price": 200},
    6: {"name": "Sauteed Sausages", "price": 200},
}
side_dishes = {
    1: {"name": "Savoury Beans", "price": 350},
    2: {"name": "Roasted Sweet Potatoes", "price": 300},
    3: {"name": "Fried Plantains", "price": 150},
    4: {"name": "Mixed Vegetable Salad", "price": 150},
    5: {"name": "Boiled Yam", "price": 150},
}
soups_and_swallow = {
    1: {"name": "Eba", "price": 100},
    2: {"name": "Poundo Yarn", "price": 100},
    3: {"name": "Semo", "price": 100},
    4: {"name": "Atama Soup", "price": 450},
    5: {"name": "Egusi Soup", "price": 400},
}
beverages = {
    1: {"name": "Water", "price": 200},
    2: {"name": "Glass Drink (35cm)", "price": 150},
    3: {"name": "PET Drink (35cl)", "price": 300},
    4: {"name": "PET Drink (50cl)", "price": 350},
    5: {"name": "Glass/Canned Malt", "price": 500},
    6: {"name": "Fresh Yo", "price": 600},
    7: {"name": "Pineapple Juice", "price": 350},
    8: {"name": "Mango Juice", "price": 350},
    9: {"name": "Zobo Drink", "price": 350},
}

cart_amount = []  # Customers empty cart array defined here.

# FUNCTION CATALOGUE STARTS HERE...

def displayMenu(dict1, dict2, dict3, dict4, dict5): # Function to display menu
    # Create main window
    root = tk.Tk()
    root.title("Menu")
    root.geometry("300x900")

    menu_label = tk.Label(root, text="\n1. RICE AND SPAGHETTI\n")
    menu_label.pack()

    for i in dict1:
        menu_label = tk.Label(root, text=f'{i}. {dict1[i]['name']} - N{dict1[i]['price']}')
        menu_label.pack()

    menu_label = tk.Label(root, text="\n2. PROTEINS\n")
    menu_label.pack()

    for i in dict2:
        menu_label = tk.Label(root, text=f'{i}. {dict2[i]['name']} - N{dict2[i]['price']}')
        menu_label.pack()

    menu_label = tk.Label(root, text="\n3. SIDE DISHES\n")
    menu_label.pack()

    for i in dict3:
        menu_label = tk.Label(root, text=f'{i}. {dict3[i]['name']} - N{dict3[i]['price']}')
        menu_label.pack()

    menu_label = tk.Label(root, text="\n4. SOUPS AND SWALLOW\n")
    menu_label.pack()

    for i in dict4:
        menu_label = tk.Label(root, text=f'{i}. {dict4[i]['name']} - N{dict4[i]['price']}')
        menu_label.pack()

    menu_label = tk.Label(root, text="\n5. BEVERAGES\n")
    menu_label.pack()

    for i in dict5:
        menu_label = tk.Label(root, text=f'{i}. {dict5[i]['name']} - N{dict5[i]['price']}')
        menu_label.pack() 


def locatePrice(submenu, order): # Function to locate price of order from dictionary
    if submenu == 1:  # Rice and pasta
        price = rice_and_pasta[order]["price"]

    elif submenu == 2:  # Proteins
        price = proteins[order]["price"]

    elif submenu == 3:  # Side dishes
        price = side_dishes[order]["price"]

    elif submenu == 4:  # soup and swallow
        price = soups_and_swallow[order]["price"]

    elif submenu == 5:  # beverages
        price = beverages[order]["price"]
    else:  # error handling
        print("Invalid Input")
    return price


def locateName(submenu, order): # Function to locate name of order from dictionary
    if submenu == 1:  # Rice and pasta
        name = rice_and_pasta[order]["name"]

    elif submenu == 2:  # Proteins
        name = proteins[order]["name"]

    elif submenu == 3:  # Side dishes
        name = side_dishes[order]["name"]

    elif submenu == 4:  # soup and swallow
        name = soups_and_swallow[order]["name"]

    elif submenu == 5:  # beverages
        name = beverages[order]["name"]
    else:  # error handling
        print("Invalid Input")
    return name


def addCart(arr): # Function to add prices of items in cart
    total_price = 0
    for num in arr:
        total_price += num
    return total_price


def calculateDiscount(total): # Function to calculate discount
    if total <= 1000:
        # No discount
        messagebox.showinfo("Info", "No discount")
        messagebox.showinfo("Discount", f"Total Amount: N{total}")
    elif total > 1000 and total < 2500:
        # 10% discount
        discount = total * 1.1
        messagebox.showinfo("Info", "You have received a 10% discount")
        messagebox.showinfo("Discount", f"Total Amount: N{discount}")
    elif total >= 2500 and total < 5000:
        # 15% discount
        discount = total * 1.15
        messagebox.showinfo("Info", "You have received a 15% discount")
        messagebox.showinfo("Discount", f"Total Amount: N{discount}")
    elif total >= 5000:
        # 15% discount
        discount = total * 1.25
        messagebox.showinfo("Info", "You have received a 25% discount")
        messagebox.showinfo("Discount", f"Total Amount: N{discount}")
    else:
        # Error handling
        messagebox.showinfo("Error", "Something went wrong... Try again")


def takeOrder(name, arr): # Function to take all orders

    # Function for take order button

    def more_button():
        submenu = int(submenu_entry.get())
        order = int(order_entry.get())
        quantity = int(quantity_entry.get())

        item_price = locatePrice(submenu, order)
        item_name = locateName(submenu, order)
        amount = item_price * quantity
        arr.append(amount)

        messagebox.showinfo("cart", f"{name}, you have successfully added {item_name} x{quantity} to your cart")
        result = messagebox.askyesno("More","Would you like to order anything else?")
        if result: # If true
            takeOrder(name,arr)
        else:
            total = addCart(arr)
            calculateDiscount(total)

    root = tk.Tk()
    root.title("Customers Order")
    root.geometry("300x200")

    # Create entry fields for user input
    submenu_label = tk.Label(root, text="Select menu category:")
    submenu_label.pack()
    submenu_entry = tk.Entry(root)  # Entry widget for last submenu
    submenu_entry.pack()

    order_label = tk.Label(root, text="What would you like to order today?")
    order_label.pack()
    order_entry = tk.Entry(root)  # Entry widget for last order
    order_entry.pack()

    quantity_label = tk.Label(root, text="How many would you like? ")
    quantity_label.pack()
    quantity_entry = tk.Entry(root)  # Entry widget for last quantity
    quantity_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=more_button)
    submit_button.pack()


def button_click(): # Function for handling name button and calling takeorder function
    name = name_entry.get()
    takeOrder(name, cart_amount)


# FUNCTION CATALOGUE ENDS HERE

# MAIN STARTS HERE...

displayMenu(rice_and_pasta, proteins, side_dishes, soups_and_swallow, beverages)

# Create name collection window
root = tk.Tk()
root.title("Customer Name")
root.geometry("250x100")

# Create entry fields for users name
name_label = tk.Label(root, text="Enter your name")
name_label.pack()
name_entry = tk.Entry(root)  # Entry widget for last name
name_entry.pack()

# button
submit_button = tk.Button(root, text="Submit", command=button_click)
submit_button.pack()

root.mainloop()
