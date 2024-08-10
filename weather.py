import tkinter as tk
import requests
import json

api_key = 'e0ac40123b5739aa83136630333c6271'

def get_weather():
 city = city_entry.get()
 url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
 response = requests.get(url)
 weather_data = response.json()
 temperature_label.config(text=f'Temperature: {round(weather_data["main"]["temp"] - 273.15, 2)}°C')
 humidity_label.config(text=f'Humidity: {weather_data["main"]["humidity"]}%')
 description_label.config(text=f'Description: {weather_data["weather"][0]["description"]}')

root = tk.Tk()
root.title('Weather App')

city_label = tk.Label(root, text='City:')
city_label.grid(row=0, column=0)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2)

temperature_label = tk.Label(root, text='Temperature:')
temperature_label.grid(row=2, column=0)

humidity_label = tk.Label(root, text='Humidity:')
humidity_label.grid(row=3, column=0)

description_label = tk.Label(root, text='Description:')
description_label.grid(row=4, column=0)

root.mainloop()