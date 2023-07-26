import requests
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

current_date_only = datetime.today().date().strftime("%d-%m-%Y")
name = input("your city name= ").capitalize()
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q={}&appid=c007f3fc3a422083d719d41a4a511272".format(
        name
    )
)
weathertoday = response.json()
weather_data = {
    "Temperature": weathertoday["main"]["temp"] - 273.15,
    "Humidity": weathertoday["main"]["humidity"],
    "Weather Description": weathertoday["weather"][0]["description"],
    "City": weathertoday["name"],
}
weather = [weather_data]
weather_city = pd.DataFrame(weather)
print(weather_city.head())
