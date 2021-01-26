from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkcalendar import *
import datetime as dt
import json

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

# ========== import json data ==========
with open('consumptions.json') as c:
  data = json.load(c)

# ========== INPUT VARAIBLES ==========
device = StringVar()
wattage = DoubleVar()
hours = IntVar()
minutes = IntVar()
rate = DoubleVar()

# ========== GET TOTAL COST FUNCTION =============
def get_total_cost():
  total = 0.00
  for consume in data['consumptions']:
    if consume['date'] == f"{dt.datetime.now():%m/%d/%Y}":
      total += consume['cost']
  return total

# ========== GET CONSUMPTION DATA FUNCTION =============
def get_consumption_data (tv, current_date, data):
  tv['columns'] = ("Wattage", "No. of Hours Used", "Cost")

  # Format Columns
  tv.column("#0", width=50, anchor=CENTER)
  tv.column("Wattage", width=50, anchor=CENTER)
  tv.column("No. of Hours Used", width=80, anchor=CENTER)
  tv.column("Cost", width=80, anchor=CENTER)

  # Create Headings
  tv.heading("#0", text="Device/s")
  tv.heading("Wattage", text="Wattage")
  tv.heading("No. of Hours Used", text="No. of Hours Used")
  tv.heading("Cost", text="Cost")
  tv.place(relwidth=0.96, relheight=0.82, relx=0.02, rely=0.03)
  for consume in data:
    if consume['date'] == current_date:
      tv.insert(parent='', 
                index='end', 
                iid=consume, 
                text=consume['device'], 
                values=(consume['wattage'], 
                    str(consume['time']['hours']) + ':' + str(consume['time']['minutes']), 
             "₱ " + str(consume['cost'])))
  return tv

# ===== BOOLEAN VALIDATION ======
def validation ():
  value = FALSE
  d = device.get()
  w = wattage.get()
  h = hours.get()
  m = minutes.get()
  r = rate.get()
  if d == '' or (w == 0.00 or w == '') or (h == 0  or h ==  '') or (m == '' or m == 0) or (r == 0.00 or r == ''):
    messagebox.showinfo("Title", "All fields required!")
    value = FALSE
  else:
    value = TRUE
  return value

# =======  AUTO UPDATE NEWLY INSERTED DATA =====
def auto_update (newData):
  lblF1 = LabelFrame(registration, text="LIST OF APPLIANCES USED TODAY", font=("Segoe UI", 10, "underline"), bg="#b5b5b5")
  tv = ttk.Treeview(lblF1)
  get_consumption_data (tv, f"{dt.datetime.now():%m/%d/%Y}", newData)
  
# function to add to JSON 
def write_json(data, filename='consumptions.json'): 
  with open(filename,'w') as f: 
    json.dump(data, f, indent=2) 

# ==== ON REGISTRATION DEVICE =====
def on_register ():
  try:
    current_date = f"{dt.datetime.now():%m/%d/%Y}"
    d = device.get()
    w = wattage.get()
    h = hours.get()
    m = minutes.get()
    r = rate.get()
    c = 45

    if validation():
      time = { "hours": h, "minutes": m }
      newData = {
        "date": current_date, "device": d, "wattage": w,
        "time": time, "rate": r, "cost": c
      }

      if (m >= 60):
        messagebox.showwarning(title="Something went wrong!", message="Beyond 60 minutes is absolutely invalid you dummy ass...")
      else:
        current_data = data['consumptions'] # SELECT CURRENT DATA
        current_data.append(newData) # INSERT or APPEND NEW DATA
        print({"consumptions": current_data}) # PRINT UPDATED DATA IN CONSOLE
        registration_tab() # AUTO REFRESH TREEVIEW
        write_json({"consumptions": current_data})# UPLOAD DATA INTO JSON DATA
        messagebox.showinfo("New Data Inserted",
                            "\nDate: " + str(current_date) + "\n"
                            "Device: " + str(d) + "\n"
                            "Wattage: " + str(w) + "\n"
                            "Time: " + str(h) + ":" + str(m) + "\n"
                            "Rate: " + str(r) + "\n"
                            "Cost: " + str(c)) # SHOW NEWLY DATA INSERTED
        on_cancel() # CLEAR ENTRY FIELDS

  except ValueError:
    messagebox.showerror(title="Something went wrong!", message="Oops!  That was no valid number.  Try again...")
  except OSError as err:
    messagebox.showerror(title="Something went wrong!", message="OS error: {0}".format(err))
  except (RuntimeError, TypeError, NameError) as er:
    messagebox.showerror(title="Something went wrong!", message="Run error: " + str(er))
  except:
    messagebox.showwarning(title="Something went wrong!", message="Opps!! Invalid inputs, it should be a number!")

# ===== ON CANCEL REGISTRATION FIELDS ======
def on_cancel ():
  device.set('')
  wattage.set(0.0)
  hours.set(0)
  minutes.set(0)
  rate.set(0.0)


def home_tab():
    lblHome = Label(home,text="HOME", font=("Segoe UI", 40),relief="raised")
    lblHome.place(relx=0.5, rely=0.2)


def registration_tab():

    Label(registration, text="DEVICE REGISTRATION", font=("Segoe UI", 24, "underline")).place(rely=0.02, relx=0.28)
    # Label(registration, text=f"Today is{dt.datetime.now(): %m/%d/%Y}", font=("Segoe UI", 20, "underline")).place(rely=0.09, relx=0.32)

    lblF1 = LabelFrame(registration, text="LIST OF APPLIANCES USED TODAY", font=("Segoe UI", 10, "underline"),
                     bg="#b5b5b5")
    lblF1.place(relwidth=0.96, relheight=0.57, relx=0.02, rely=0.40)

    Label(registration, text="Device Name:", font=("Segoe UI", 10)).place(relx=0.05, rely=.2)
    Label(registration, text="Wattage:", font=("Segoe UI", 10)).place(relx=0.335, rely=.2)
    Label(registration, text="Time:", font=("Segoe UI", 10)).place(relx=0.555, rely=.2)
    Label(registration, text="HH", font=("Segoe UI", 8)).place(relx=0.61, rely=.165)
    Label(registration, text="MM", font=("Segoe UI", 8)).place(relx=0.665, rely=.165)
    Label(registration, text=":", font=("Segoe UI", 10)).place(relx=0.645, rely=.2)
    Label(registration, text="KWH Rate:", font=("Segoe UI", 10)).place(relx=0.75, rely=.2)


    Entry(registration, textvar=device, font=("Segoe UI", 11), width=15).place(relx=0.15, rely=0.197)
    Entry(registration, textvar=wattage, font=("Segoe UI", 12), width=10).place(relx=0.405, rely=0.197)
    Entry(registration, textvar=hours, font=("Segoe UI", 12), width=3).place(relx=0.605, rely=0.197)
    Entry(registration, textvar=minutes, font=("Segoe UI", 12), width=3).place(relx=0.66, rely=0.197)
    Entry(registration, textvar=rate, font=("Segoe UI", 12), width=10).place(relx=0.845, rely=0.197)

    Button(registration, padx=2, pady=3, font=('arial', 12), width=6, text="SAVE", bd=2, bg="#b5b5b5", command=on_register).place(relx=0.75, rely=0.31) # REGISTRATION BUTTON
    Button(registration, padx=2, pady=3, font=('arial', 12), width=6, text="CANCEL", bd=2, bg="#b5b5b5", command=on_cancel).place(relx=0.85, rely=0.31) # CANCEL BUTTON

    # Note
    lblNote = Label(registration,
                    text="Note: Please go to Home Tab and click 'help' button to see the average rate of consumption of every devices.",
                    font=("Segoe UI", 8), relief="sunken")
    lblNote.place(relx=0.02, rely=0.345)


    lblTotal = Label(lblF1, text="Total Cost:", font=("Segoe UI", 10, "bold"))
    lblTotal.place(relx=0.7, rely=0.885)
    txtOverall = Entry(lblF1, font=("Segoe UI", 12), width=13)
    txtOverall.insert(0, get_total_cost())
    txtOverall.configure(state=tk.DISABLED)
    txtOverall.place(relx=0.81, rely=0.87)


    #Treeview
    tv = ttk.Treeview(lblF1)
    tvData = data['consumptions']
    get_consumption_data (tv, f"{dt.datetime.now():%m/%d/%Y}", tvData)

def consumption_tab():
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

    # Home tab information
    home_tab()

    # Device Registration
    registration_tab()

    # Track Consumption Tab
    consumption_tab()


# application start
if __name__ == "__main__":
  start()
  root.mainloop()