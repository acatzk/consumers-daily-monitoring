from tkinter import *
from tkinter import ttk
import tkinter as tk


root = Tk()
root.title("Electric Billing System")
root.geometry('1050x720')


# Tab Control
tabControl = ttk.Notebook(root)
tabControl.pack(fill="both", expand=1)

home = tk.Frame(tabControl,background="#323743", width=1000, height= 680)
registration = tk.Frame(tabControl, background="#323743", width=1000, height= 680)
total = tk.Frame(tabControl, background="#323743", width=1000, height= 680)

home.pack(fill="both", expand=1)
registration.pack(fill="both", expand=1)
total.pack(fill="both", expand=1)


tabControl.add(home, text='Home')
tabControl.add(registration, text='Daily Registration')
tabControl.add(total, text='Total Consumption')



# Registration Elements
account_no = tk.Label(registration, text="Account Number:", font=("Segoe UI", 10)).grid(column=0, row=0, columnspan=1, padx=10, pady=25)
e_account = ttk.Entry(registration, width = 20).grid(row=0, column=1)
meter_no = tk.Label(registration, text="Meter Number:", font=("Segoe UI", 10)).grid(column=2, row=0, padx=10, pady=10)
e_meter = ttk.Entry(registration, width = 20).grid(row=0, column=3)
first = ttk.Label(registration, text="First Name:", font=("Segoe UI", 10)).grid(column=0, row=1, padx= 10, pady= 10)
e_first = ttk.Entry(registration, width = 20).grid(row=1, column=1)
middle = ttk.Label(registration, text="Middle Name:", font=("Segoe UI", 10)).grid(column=2, row=1, padx=10, pady=10)
e_middle = ttk.Entry(registration, width = 20).grid(row=1, column=3)
last = ttk.Label(registration, text="Last Name:", font=("Segoe UI", 10)).grid(column=4, row=1, padx=10, pady=10)
e_last = ttk.Entry(registration, width = 20).grid(row=1, column=5)
address = ttk.Label(registration, text="Address:", font=("Segoe UI", 10), width= 8, anchor= CENTER).grid(column=0, row=2, padx=10, pady=10)
e_address = ttk.Entry(registration, width = 70).grid(row=2, column=0, columnspan= 6)
meter_no = ttk.Label(registration, text="Address:", font=("Segoe UI", 10), width= 8, anchor= CENTER).grid(column=0, row=2, padx=10, pady=10)

root.mainloop()