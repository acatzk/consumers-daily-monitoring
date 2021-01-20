from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *


root=Tk()
root.title("Consumer's Daily Electric Consumption Monitoring Software")
root.minsize(width=1050,height=720)

#====================================================================================================================
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
tabControl.add(total, text='Track Consumption')

#===================================================================================================================
#Daily Registration Tab

title = Label(registration, text ="DEVICE REGISTRATION", font=("Segoe UI", 24, "underline"))
title.place(rely = 0.02, relx = 0.28)
#appliance = Label(registration, text ="Appliances:", font=("Segoe UI", 12))
#appliance.place(rely = 0.15, relx = 0.02)

Lb1 = LabelFrame(registration, text ="LIST OF APPLIANCES USED TODAY",font=("Segoe UI", 10, "underline"), bg = "#b5b5b5")
Lb1.place (relwidth = 0.96,relheight= 0.57, relx = 0.02, rely = 0.40)

#Treeview
tree = ttk.Treeview (Lb1)
#Define columns
tree['columns'] = ("Appliance", "Wattage","No. of Hours Used", "Total Cost")

#Format Columns
tree.column("#0", width=2, minwidth=25)
tree.column("Appliance", width=80, anchor=W)
tree.column("Wattage", width= 50, anchor=CENTER)
tree.column("No. of Hours Used", width=80, anchor=CENTER)
tree.column("Total Cost", width=120, anchor=W)

#Create Headings
tree.heading("#0", text= "No.", anchor=W)
tree.heading("Appliance", text= "Appliance", anchor=W)
tree.heading("Wattage", text= "Wattage", anchor=W)
tree.heading("No. of Hours Used", text= "No. of Hours Used", anchor=W)
tree.heading("Total Cost", text= "Total Cost", anchor=W)

#Add Data
tree.insert(parent='', index='end', iid=0, text='', values="")
tree.place(relwidth = 0.96,relheight=0.96, relx = 0.02, rely = 0)

#==================================================================================================================

#Track Consumption Tab
title1 = Label(total, text ="TRACK YOUR CONSUMPTION", font=("Segoe UI", 24, "underline"))
title1.place(rely = 0.028, relx = 0.24)
frm_label = tk.Label(total, text="from:", font=("Segoe UI", 12))
frm_label.place(relx= 0.12, rely= 0.16, anchor=NW)
frm_dent = DateEntry(total, front=('arial', 14, 'bold'), bd=5, width=25, borderwidth=2, date_pattern="mm/dd/yyyy")
frm_dent.place(relx= 0.2, rely=0.165, anchor=NW)
to_label = tk.Label(total, text="to:", font=("Segoe UI", 12))
to_label.place(relx= 0.56, rely=0.16)
to_dent = DateEntry(total, front=('arial', 14, 'bold'), bd=5, width=25, borderwidth=2, date_pattern="mm/dd/yyyy")
to_dent.place(relx= 0.61, rely=0.165)
#button
T_button = Button(total, padx =3, pady = 4, font=('arial', 12), width= 10, text="TRACK",bd = 2, bg="#b5b5b5")
T_button.place(relx = 0.451, rely = 0.26)

#labelFrame2
Lb2 = LabelFrame(total, text ="RESULT",font=("Segoe UI", 10, "underline"), bg = "#b5b5b5")
Lb2.place (relwidth = 0.9,relheight= 0.57, relx = 0.05, rely = 0.38)
fr= Frame(Lb2, bg="white")
fr.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.02)

fr_label = tk.Label(fr, text="from:", font=("Segoe UI", 12))
fr_label.place(relx= 0.06, rely=0.06)
fr_entry = Entry(fr, font=("Segoe UI", 12), width= 20)
fr_entry.place(relx= 0.16, rely=0.06)
to_label = tk.Label(fr, text="to:", font=("Segoe UI", 12))
to_label.place(relx= 0.52, rely=0.06)
to_entry = Entry(fr, font=("Segoe UI", 12), width= 20)
to_entry.place(relx= 0.60, rely=0.06)
total_KWH = tk.Label(fr, text="Total KWH:", font=("Segoe UI", 12))
total_KWH.place(relx= 0.02, rely=0.3)
KWH_entry = Entry(fr, font=("Segoe UI", 12), width= 20)
KWH_entry.place(relx= 0.16, rely=0.3)
total_cost = tk.Label(fr, text="Total Cost:", font=("Segoe UI", 12))
total_cost.place(relx= 0.45, rely=0.3)
cost_entry = Entry(fr, font=("Segoe UI", 12), width= 20)
cost_entry.place(relx= 0.60, rely=0.3)

#Clear Button
C_button = Button(fr, padx =3, pady = 4, font=('arial', 12), width= 10, text="CLEAR",bd = 2, bg="#b5b5b5")
C_button.place(relx = 0.8, rely = 0.8)
#StringVar
#From_Date = StringVar()
#to = StringVar()

#cal1 = Calendar(total, selectmode="day", year=2021, month=1, day=20, date_pattern= "dd/mm/y", font=('arial', 16, 'bold'))
#cal1.grid(row=0, column=0, padx=10)

root.mainloop()