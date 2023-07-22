import requests
from datetime import datetime
current_date_only = datetime.today().date().strftime("%d-%m-%Y")
response=requests.get('https://api.openweathermap.org/data/2.5/weather?q=Kathmandu&appid=c007f3fc3a422083d719d41a4a511272')
weathertoday = response.json()
print(weathertoday)
weather_data = {
    "Temperature": weathertoday["main"]["temp"],
    "Humidity": weathertoday["main"]["humidity"],
    "Weather Description": weathertoday["weather"][0]["description"],
    "City": weathertoday["name"]
}
print(weather_data)
