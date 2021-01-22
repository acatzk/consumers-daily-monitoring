import requests
from tkinter import *


def weather():
    city = city_listbox.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=1818973441ac40aa99aa3d5aa227e48f".format(city)
    res = requests.get(url)
    output = res.json()

    weather_status = output['weather'][0]['description']
    temprature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']

    weather_status_label.configure(text="weather status : " + weather_status)
    temprature_label.configure(text="temprature : " + str(temprature))
    humidity_label.configure(text="Humidity : " + str(humidity))
    wind_speed_label.configure(text="wind speed  : " + str(wind_speed))


window = Tk()
window.geometry("400x350")

city_name_list = ["Ormoc", "Maasin", "Sogod", "Baybay", "Baybay","Baybay", "Baybay", "Baybay", "Baybay", "Baybay",
                  "Baybay", "Baybay", "Baybay", "Baybay", "Baybay", "Baybay", "Baybay", "Baybay"]

city_listbox = StringVar(window)
city_listbox.set("select the city")
option = OptionMenu(window, city_listbox, *city_name_list)
option.place(relx=0.325, rely=0.09, width=150)

b1 = Button(window, text="CHECK", width=6, command=weather)
b1.place(relx=0.415, rely= 0.23)

weather_status_label = Label(window, font=("times", 10, "bold"))
weather_status_label.place(relx=0.3, rely=0.4)

temprature_label = Label(window, font=("times", 10, "bold"))
temprature_label.place(relx=0.3, rely=0.5)

humidity_label = Label(window, font=("times", 10, "bold"))
humidity_label.place(relx=0.3, rely=0.6)

wind_speed_label = Label(window, font=("times", 10, "bold"))
wind_speed_label.place(relx=0.3, rely=0.7)

window.mainloop()