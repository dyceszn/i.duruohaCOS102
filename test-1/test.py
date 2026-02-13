import tkinter as tk
from tkinter import messagebox as mbox

def compSci():
    root = tk.Tk()
    root.title("Computer Science Admission")
    
    def check_admission():
        jamb = int(jamb_entry.get())
        if (jamb >= 250 and eng_var.get() not in ["D","F"] and 
            phy_var.get() not in ["D","F"] and mth_var.get() not in ["D","F"] and
            bio_var.get() not in ["D","F"] and chem_var.get() not in ["D","F"]):
            mbox.showinfo("Admission Result", "Congratulations! You meet the criteria for admission.")
        else:
            mbox.showinfo("Admission Result", "Sorry, you did not meet the criteria for admission.")

    jamb_label = tk.Label(root, text="Enter your JAMB score:")
    jamb_label.pack()

    jamb_entry = tk.Entry(root)
    jamb_entry.pack()

    subjectgrade_label = tk.Label(root, text="Select your grades for the following courses:")
    subjectgrade_label.pack()

    grades = ["A", "B", "C", "D", "F"]

    phy_label = tk.Label(root, text="Physics:")
    phy_label.pack()
    phy_var = tk.StringVar(root)
    phy_var.set(grades[0])
    phy_menu = tk.OptionMenu(root, phy_var, *grades)
    phy_menu.pack()

    chem_label = tk.Label(root, text="Chemistry:")
    chem_label.pack()
    chem_var = tk.StringVar(root)
    chem_var.set(grades[0])
    chem_menu = tk.OptionMenu(root, chem_var, *grades)
    chem_menu.pack()

    bio_label = tk.Label(root, text="Biology:")
    bio_label.pack()
    bio_var = tk.StringVar(root)
    bio_var.set(grades[0])
    bio_menu = tk.OptionMenu(root, bio_var, *grades)
    bio_menu.pack()

    mth_label = tk.Label(root, text="Mathematics:")
    mth_label.pack()
    mth_var = tk.StringVar(root)
    mth_var.set(grades[0])
    mth_menu = tk.OptionMenu(root, mth_var, *grades)
    mth_menu.pack()

    eng_label = tk.Label(root, text="English:")
    eng_label.pack()
    eng_var = tk.StringVar(root)
    eng_var.set(grades[0])
    eng_menu = tk.OptionMenu(root, eng_var, *grades)
    eng_menu.pack()

    check_button = tk.Button(root, text="Check Admission", command=check_admission)
    check_button.pack()

def massComm():
    root = tk.Tk()
    root.title("Mass Communication Admission")
    
    def check_admission():
        jamb = int(jamb_entry.get())
        if (jamb >= 230 and eng_var.get() not in ["D","F"] and 
            lit_var.get() not in ["D","F"] and mth_var.get() not in ["D","F"] and
            gov_var.get() not in ["D","F"] and crs_var.get() not in ["D","F"]):
            mbox.showinfo("Admission Result", "Congratulations! You meet the criteria for admission.")
        else:
            mbox.showinfo("Admission Result", "Sorry, you did not meet the criteria for admission.")

    jamb_label = tk.Label(root, text="Enter your JAMB score:")
    jamb_label.pack()

    jamb_entry = tk.Entry(root)
    jamb_entry.pack()

    subjectgrade_label = tk.Label(root, text="Select your grades for the following courses:")
    subjectgrade_label.pack()

    grades = ["A", "B", "C", "D", "F"]

    crs_label = tk.Label(root, text="CRS:")
    crs_label.pack()
    crs_var = tk.StringVar(root)
    crs_var.set(grades[0])
    crs_menu = tk.OptionMenu(root, crs_var, *grades)
    crs_menu.pack()

    lit_label = tk.Label(root, text="Literature:")
    lit_label.pack()
    lit_var = tk.StringVar(root)
    lit_var.set(grades[0])
    lit_menu = tk.OptionMenu(root, lit_var, *grades)
    lit_menu.pack()

    gov_label = tk.Label(root, text="Government:")
    gov_label.pack()
    gov_var = tk.StringVar(root)
    gov_var.set(grades[0])
    gov_menu = tk.OptionMenu(root, gov_var, *grades)
    gov_menu.pack()

    mth_label = tk.Label(root, text="Mathematics:")
    mth_label.pack()
    mth_var = tk.StringVar(root)
    mth_var.set(grades[0])
    mth_menu = tk.OptionMenu(root, mth_var, *grades)
    mth_menu.pack()

    eng_label = tk.Label(root, text="English:")
    eng_label.pack()
    eng_var = tk.StringVar(root)
    eng_var.set(grades[0])
    eng_menu = tk.OptionMenu(root, eng_var, *grades)
    eng_menu.pack()

    check_button = tk.Button(root, text="Check Admission", command=check_admission)
    check_button.pack()

def proceed():
    department = department_entry.get()
    if department == "Computer Science":
        compSci()
    elif department == "Mass Communication":
        massComm()
    else:
        mbox.showinfo("Invalid Department", "Please enter a valid department.")

root = tk.Tk()
root.title("Admission Check")
root.geometry("500x200")

department_label = tk.Label(root, text="Input your department:")
department_label.pack()

department_entry = tk.Entry(root)
department_entry.pack()

next_button = tk.Button(root, text="Proceed", command=proceed)
next_button.pack()

root.mainloop()
