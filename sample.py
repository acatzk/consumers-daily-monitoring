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

def hometab():
    lblHome = Label(home,text="HOME", font=("Segoe UI", 40),relief="raised")
    lblHome.place(relx=0.5, rely=0.2)


def registrationTab():
    lbltitle = Label(registration, text="DEVICE REGISTRATION", font=("Segoe UI", 24, "underline"))
    lbltitle.place(rely=0.02, relx=0.28)
    # appliance = Label(registration, text ="Appliances:", font=("Segoe UI", 12))
    # appliance.place(rely = 0.15, relx = 0.02)

    lblF1 = LabelFrame(registration, text="LIST OF APPLIANCES USED TODAY", font=("Segoe UI", 10, "underline"),
                     bg="#b5b5b5")
    lblF1.place(relwidth=0.96, relheight=0.57, relx=0.02, rely=0.40)

    lblApp = Label(registration, text="Device Name:", font=("Segoe UI", 10))
    lblWatt = Label(registration, text="Wattage:", font=("Segoe UI", 10))
    lblHour = Label(registration, text="Hours Used:", font=("Segoe UI", 10))
    lblRate = Label(registration, text="KWH Rate:", font=("Segoe UI", 10))

    lblApp.place(relx=0.02, rely=.2)
    lblWatt.place(relx=0.32, rely=.2)
    lblHour.place(relx=0.535, rely=.2)
    lblRate.place(relx=0.75, rely=.2)

    txtApp = Entry(registration, font=("Segoe UI", 11), width=15)
    txtWatt = Entry(registration, font=("Segoe UI", 12), width=10)
    txtHour = Entry(registration, font=("Segoe UI", 12), width=8)
    txtRate = Entry(registration, font=("Segoe UI", 12), width=10)

    txtApp.place(relx=0.14, rely=0.195)
    txtWatt.place(relx=0.40, rely=0.195)
    txtHour.place(relx=0.64, rely=0.195)
    txtRate.place(relx=0.845, rely=0.195)

    btnsave = Button(registration, padx=2, pady=3, font=('arial', 12), width=6, text="SAVE", bd=2, bg="#b5b5b5")
    btnsave.place(relx=0.75, rely=0.31)
    btnclr = Button(registration, padx=2, pady=3, font=('arial', 12), width=6, text="CLEAR", bd=2, bg="#b5b5b5")
    btnclr.place(relx=0.85, rely=0.31)

    # Note
    lblNote = Label(registration,
                    text="Note: Please go to Home Tab and click 'help' button to see the average rate of consumption of every devices.",
                    font=("Segoe UI", 8), relief="sunken")
    lblNote.place(relx=0.02, rely=0.345)


    lblTotal = Label(lblF1, text="Total Cost:", font=("Segoe UI", 10, "bold"))
    lblTotal.place(relx=0.7, rely=0.885)
    txtOver = Entry(lblF1, font=("Segoe UI", 12), width=13)
    txtOver.place(relx=0.81, rely=0.87)


    #Treeview
    tv = ttk.Treeview(lblF1)
    # Define columns
    tv['columns'] = ("Wattage", "No. of Hours Used", "Cost")

    # Format Columns
    tv.column("#0", width=120, minwidth=25)
    tv.column("Wattage", width=50, anchor=CENTER)
    tv.column("No. of Hours Used", width=80, anchor=CENTER)
    tv.column("Cost", width=80, anchor=E)

    # Create Headings
    tv.heading("#0", text="Device/s")
    tv.heading("Wattage", text="Wattage")
    tv.heading("No. of Hours Used", text="No. of Hours Used")
    tv.heading("Cost", text="Cost")

    # Add Data
    tv.insert(parent='', index='end', iid=0, text='', values="")
    tv.place(relwidth=0.96, relheight=0.82, relx=0.02, rely=0.03)

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
    # Track button
    btntrack = Button(total, padx=3, pady=4, font=('arial', 12), width=10, text="TRACK", bd=2, bg="#b5b5b5")
    btntrack.place(relx=0.355, rely=0.265)
    # Clear Button
    btnclear = Button(total, padx=3, pady=4, font=('arial', 12), width=10, text="CLEAR", bd=2, bg="#b5b5b5")
    btnclear.place(relx=0.525, rely=0.265)


    # labelFrame2
    lblFresult = LabelFrame(total, text="RESULT", font=("Segoe UI", 10, "underline"), bg="#b5b5b5")
    lblFresult.place(relwidth=0.9, relheight=0.57, relx=0.05, rely=0.38)
    fr = Frame(lblFresult, bg="white")
    fr.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.02)

    lbldays = tk.Label(fr, text="Total Days:", font=("Segoe UI", 12))
    lbldays.place(relx=0.02, rely=0.87)
    txtdays = Entry(fr, font=("Segoe UI", 12), width=12)
    txtdays.place(relx=0.155, rely=0.87)
    lblKWH = tk.Label(fr, text="Total KWH:", font=("Segoe UI", 12))
    lblKWH.place(relx=0.345, rely=0.87)
    txtKWH = Entry(fr, font=("Segoe UI", 12), width=12)
    txtKWH.place(relx=0.485, rely=0.87)
    lblcost = tk.Label(fr, text="Total Cost:", font=("Segoe UI", 12))
    lblcost.place(relx=0.675, rely=0.87)
    txtcost = Entry(fr, font=("Segoe UI", 12), width=12)
    txtcost.place(relx=0.815, rely=0.87)

    #treeview
    tv1 = ttk.Treeview(fr)
    # Define columns
    tv1['columns'] = ("Device/s", "Wattage", "No. of Hours Used", "Cost")

    # Format Columns
    tv1.column("#0", width=110, minwidth=25)
    tv1.column("Device/s", width=120, anchor=W)
    tv1.column("Wattage", width=40, anchor=CENTER)
    tv1.column("No. of Hours Used", width=90, anchor=CENTER)
    tv1.column("Cost", width=60, anchor=E)

    # Create Headings
    tv1.heading("#0", text="Date")
    tv1.heading("Device/s", text="Device/s")
    tv1.heading("Wattage", text="Wattage")
    tv1.heading("No. of Hours Used", text="No. of Hours Used")
    tv1.heading("Cost", text="Cost")

    # Add Data
    tv1.insert(parent='', index='end', iid=0, text='', values="")
    tv1.place(relwidth=0.96, relheight=0.8, relx=0.02, rely=0.03)



# start method
def start ():
    root.title("Consumer's Daily Electric Consumption Monitoring Software")
    root.minsize(width=1050, height=720)

    # end device registration
    registrationTab()

    # Track Consumption Tab
    consumptionTab()

    hometab()


# application start
start()
root.mainloop()