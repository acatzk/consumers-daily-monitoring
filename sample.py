from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkcalendar import *
import datetime as dt
import json
import uuid

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
dateFrom = StringVar()
dateTo = StringVar()
totalCostByDate = 0.00

# ========== GET TOTAL COST FUNCTION =============
def get_total_cost():
  total = 0.00
  for consume in data['consumptions']:
    if consume['date'] == f"{dt.datetime.now():%m/%d/%Y}":
      total += consume['cost']
  return "₱ " + str(round(total, 2))

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
                iid=consume['id'], 
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
  if d == '' or (w == 0.00 or w == '') or (h == 0  or h ==  '') or (m == '') or (r == 0.00 or r == ''):
    messagebox.showinfo("Title", "All fields required!")
    value = FALSE
  else:
    value = TRUE
  return value

# function to add to JSON 
def write_json(data, filename='consumptions.json'): 
  with open(filename,'w') as f: 
    json.dump(data, f, indent=2) 

# cost formula
def cost_formula (watts, hours, minutes, rate):
  return round(((watts / 1000) * (hours + (minutes/60)) * (rate)), 2)


# ==== ON REGISTRATION DEVICE =====
def on_register ():
  try:
    id = uuid.uuid1()
    current_date = f"{dt.datetime.now():%m/%d/%Y}"
    d = device.get()
    w = wattage.get()
    h = hours.get()
    m = minutes.get()
    r = rate.get()
    c = cost_formula(w, h, m, r)
    if validation():
      time = { "hours": h, "minutes": m }
      newData = {
        "id": id.hex, "date": current_date, 
        "device": d, "wattage": w,
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
                            "Cost: ₱" + str(c)) # SHOW NEWLY DATA INSERTED
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


# ===== ON REMOVE DATA IN TREEVIEW & JSON FILE
def on_remove (tv):
  selected_id = tv.selection()
  current_data = data['consumptions']
  if (selected_id):
    MsgBox = tk.messagebox.askquestion ('Are you sure','Do you want to delete?', icon = 'info')
    if MsgBox == 'yes':
      for newdata in current_data:
        for id in selected_id:
          if (newdata['id'] == id):
            tv.delete(id)           
            current_data = data['consumptions'] # SELECT CURRENT DATA
            current_data.remove(newdata) # INSERT or APPEND NEW DATA
            write_json({"consumptions": current_data})# UPLOAD DATA INTO JSON DATA
      messagebox.showinfo(title="Successful", message="Successfully deleted!")
    else:
      return
  else:
    messagebox.showinfo(title="Opps!!", message="Please select item/s to delete")


def home_tab():
    lblHome = Label(home,text="HOME", font=("Segoe UI", 40),relief="raised")
    lblHome.place(relx=0.5, rely=0.2)


def registration_tab():

    Label(registration, text="DEVICE REGISTRATION", font=("Segoe UI", 24, "underline")).place(rely=0.02, relx=0.28)
    # Label(registration, text=f"Today is{dt.datetime.now(): %m/%d/%Y}", font=("Segoe UI", 20, "underline")).place(rely=0.09, relx=0.32)

    lblF1 = LabelFrame(registration, text="LIST OF APPLIANCES USED TODAY", font=("Segoe UI", 10, "underline"),
                     bg="#b5b5b5")
    lblF1.place(relwidth=0.96, relheight=0.57, relx=0.02, rely=0.40)

    #Treeview
    tv = ttk.Treeview(lblF1)

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

    Button(registration, padx=2, pady=3, font=('arial', 12), width=6, text="Save", bd=2, bg="#b5b5b5", command=on_register).place(relx=0.75, rely=0.31) # REGISTRATION BUTTON
    Button(registration, padx=2, pady=3, font=('arial', 12), width=9, text="Cancel", bd=2, bg="#b5b5b5", command=on_cancel).place(relx=0.85, rely=0.31) # CANCEL BUTTON
    Button(lblF1, padx=2, pady=3, font=('arial', 11), width=20, text="Remove selected items", bd=2, bg="#b5b5b5", command=lambda:on_remove(tv)).place(relx=0.02, rely=0.87) # REMOVE DATA IN TREEVIEW & JSON

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

    tvData = data['consumptions']
    get_consumption_data (tv, f"{dt.datetime.now():%m/%d/%Y}", tvData)


# ON TRACK RECORDS BY DATE
def on_track_records (tv1, dfrom, dto, txtCost, txtKWH, txtdevice):
  df = str('{:02d}'.format(dfrom.get_date().month)) + "/" + str('{:02d}'.format(dfrom.get_date().day)) + "/" + str(dfrom.get_date().year)
  dt = str('{:02d}'.format(dto.get_date().month)) + "/" + str('{:02d}'.format(dto.get_date().day)) + "/" + str(dto.get_date().year)
  total_data_by_date(tv1, df, dt, txtCost, txtKWH, txtdevice)
  for record in tv1.get_children():
    tv1.delete(record)
  for consume in data['consumptions']:
    if (consume['date'] >= str(df)) and consume['date'] <= str(dt):
      tv1.insert(parent='', 
                index='end', 
                iid=consume['id'], 
                text=consume['date'], 
                values=(consume['device'],
                        consume['wattage'], 
                    str(consume['time']['hours']) + ':' + str(consume['time']['minutes']), 
             "₱ " + str(consume['cost'])))
  txtdevice.delete(0,END)
  td = len(tv1.get_children())
  td = list(str(td))
  txtdevice.insert(0,max(td))
  return tv1


# CLEAR TREEVIEW RECORDS
def on_clear_records (tv1,txtCost,txtdevice,txtKWH):
  for record in tv1.get_children():
    tv1.delete(record)

  txtKWH.delete(0,END)
  txtCost.delete(0,END)
  txtdevice.delete(0,END)
  return tv1


# GET TOTAL DAYS, KWH AND COST BY DATE
def total_data_by_date (tv1, dfrom, dto, txtCost, txtKWH, txtdevice):
  totalCost = 0.00
  totalKWH = 0.00
  txtKWH.delete(0,END)
  txtCost.delete(0,END)

  for consume in data['consumptions']:
    if (consume['date'] >= str(dfrom)) and consume['date'] <= str(dto):
      totalCost += consume['cost']
      totalKWH += ((consume['wattage'] / 1000) * ((consume['time']['hours']) + ((consume['time']['minutes']) / 60)))

  txtCost.insert(0,"₱ " + str(round(totalCost, 2)))
  txtKWH.insert(0, str(round(totalKWH, 2)))
  return

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

    # labelFrame2
    lblFresult = LabelFrame(total, text="RESULT", font=("Segoe UI", 10, "underline"), bg="#b5b5b5")
    lblFresult.place(relwidth=0.9, relheight=0.57, relx=0.05, rely=0.38)
    fr = Frame(lblFresult, bg="white")
    fr.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.02)

    #treeview
    tv1 = ttk.Treeview(fr)


    # Track button
    btntrack = Button(total, padx=3, pady=4, font=('arial', 12), width=10, text="TRACK", bd=2, bg="#b5b5b5", command=lambda:on_track_records(tv1, dentfrom, dentto, txtCost, txtKWH, txtdevice))
    btntrack.place(relx=0.355, rely=0.265)
    # Clear Button
    btnclear = Button(total, padx=3, pady=4, font=('arial', 12), width=10, text="CLEAR", bd=2, bg="#b5b5b5", command=lambda:on_clear_records(tv1,txtCost,txtdevice,txtKWH))
    btnclear.place(relx=0.525, rely=0.265)

    lbldevice = tk.Label(fr, text="Total Device:", font=("Segoe UI", 12))
    lbldevice.place(relx=0.02, rely=0.87)
    txtdevice = Entry(fr, font=("Segoe UI", 12), width=12)
    txtdevice.place(relx=0.155, rely=0.87)
    lblKWH = tk.Label(fr, text="Total KWH:", font=("Segoe UI", 12))
    lblKWH.place(relx=0.36, rely=0.87)
    txtKWH = Entry(fr, font=("Segoe UI", 12), width=12)
    txtKWH.place(relx=0.485, rely=0.87)
    lblcost = tk.Label(fr, text="Total Cost:", font=("Segoe UI", 12))
    lblcost.place(relx=0.69, rely=0.87)
    txtCost = Entry(fr, font=("Segoe UI", 12), width=12)
    txtCost.place(relx=0.815, rely=0.87)

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