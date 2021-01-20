from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *


root = Tk()

tabControl = ttk.Notebook(root)
tabControl.pack(fill="both", expand=1)

home = tk.Frame(tabControl, background="#323743", width=1000, height=680)
registration = tk.Frame(tabControl, background="#323743", width=1000, height=680)
total = tk.Frame(tabControl, background="#323743", width=1000, height=680)

home.pack(fill="both", expand=1)
registration.pack(fill="both", expand=1)
total.pack(fill="both", expand=1)

tabControl.add(home, text='Home')
tabControl.add(registration, text='Daily Registration')
tabControl.add(total, text='Track Consumption')

def registrationTab():
    lbltitle = Label(registration, text="DEVICE REGISTRATION", font=("Segoe UI", 24, "underline"))
    lbltitle.place(rely=0.02, relx=0.28)
    # appliance = Label(registration, text ="Appliances:", font=("Segoe UI", 12))
    # appliance.place(rely = 0.15, relx = 0.02)

    lblF1 = LabelFrame(registration, text="LIST OF APPLIANCES USED TODAY", font=("Segoe UI", 10, "underline"),
                     bg="#b5b5b5")
    lblF1.place(relwidth=0.96, relheight=0.57, relx=0.02, rely=0.40)

    lblTotal = Label(lblF1, text="Overall Total Cost:", font=("Segoe UI", 10, "bold"))
    lblTotal.place(relx=0.62, rely=0.85)
    txtOver = Entry(lblF1, font=("Segoe UI", 12), width=13)
    txtOver.place(relx=0.81, rely=0.835)

    #Treeview
    tv = ttk.Treeview(lblF1)
    # Define columns
    tv['columns'] = ("Wattage", "No. of Hours Used", "Total Cost")

    # Format Columns
    tv.column("#0", width=120, minwidth=25)
    tv.column("Wattage", width=50, anchor=CENTER)
    tv.column("No. of Hours Used", width=80, anchor=CENTER)
    tv.column("Total Cost", width=80, anchor=E)

    # Create Headings
    tv.heading("#0", text="Device/s")
    tv.heading("Wattage", text="Wattage")
    tv.heading("No. of Hours Used", text="No. of Hours Used")
    tv.heading("Total Cost", text="Total Cost")

    # Add Data
    tv.insert(parent='', index='end', iid=0, text='', values="")
    tv.place(relwidth=0.96, relheight=0.82, relx=0.02, rely=0)

def consumptionTab():
    lbltitle = Label(total, text="TRACK YOUR CONSUMPTION", font=("Segoe UI", 24, "underline"))
    lbltitle.place(rely=0.028, relx=0.24)
    lblfrom = tk.Label(total, text="from:", font=("Segoe UI", 12))
    lblfrom.place(relx=0.12, rely=0.16, anchor=NW)
    dentfrom = DateEntry(total, front=('arial', 14, 'bold'), bd=5, width=25, borderwidth=2, date_pattern="mm/dd/yyyy")
    dentfrom.place(relx=0.2, rely=0.165, anchor=NW)
    lblto = tk.Label(total, text="to:", font=("Segoe UI", 12))
    lblto.place(relx=0.56, rely=0.16)
    dentto = DateEntry(total, front=('arial', 14, 'bold'), bd=5, width=25, borderwidth=2, date_pattern="mm/dd/yyyy")
    dentto.place(relx=0.61, rely=0.165)
    # button
    btntrack = Button(total, padx=3, pady=4, font=('arial', 12), width=10, text="TRACK", bd=2, bg="#b5b5b5")
    btntrack.place(relx=0.451, rely=0.26)

    # labelFrame2
    lblFresult = LabelFrame(total, text="RESULT", font=("Segoe UI", 10, "underline"), bg="#b5b5b5")
    lblFresult.place(relwidth=0.9, relheight=0.57, relx=0.05, rely=0.38)
    fr = Frame(lblFresult, bg="white")
    fr.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.02)

    lbldays = tk.Label(fr, text="Total Days:", font=("Segoe UI", 12))
    lbldays.place(relx=0.06, rely=0.09)
    txtdays = Entry(fr, font=("Segoe UI", 12), width=20)
    txtdays.place(relx=0.2, rely=0.09)
    lblKWH = tk.Label(fr, text="Total KWH:", font=("Segoe UI", 12))
    lblKWH.place(relx=0.06, rely=0.25)
    txtKWH = Entry(fr, font=("Segoe UI", 12), width=20)
    txtKWH.place(relx=0.2, rely=0.25)
    lblcost = tk.Label(fr, text="Total Cost:", font=("Segoe UI", 12))
    lblcost.place(relx=0.06, rely=0.42)
    txtcost = Entry(fr, font=("Segoe UI", 12), width=20)
    txtcost.place(relx=0.2, rely=0.42)

    # Clear Button
    btnclear = Button(fr, padx=3, pady=4, font=('arial', 12), width=10, text="CLEAR", bd=2, bg="#b5b5b5")
    btnclear.place(relx=0.8, rely=0.8)
    # StringVar
    # From_Date = StringVar()
    # to = StringVar()

    # cal1 = Calendar(total, selectmode="day", year=2021, month=1, day=20, date_pattern= "dd/mm/y", font=('arial', 16, 'bold'))
    # cal1.grid(row=0, column=0, padx=10)

# start method
def start ():
    root.title("Consumer's Daily Electric Consumption Monitoring Software")
    root.minsize(width=1050, height=720)

    # end device registration
    registrationTab()

    # Track Consumption Tab
    consumptionTab()


# application start
start()
root.mainloop()