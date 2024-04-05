import requests
from datetime import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

account_sid = os.getenv("account_sid")
print(account_sid)

key = "******************"
lat=51.5072
lon=0.1276
weather_params= {
    "lat": lat,
    "lon": lon,
    "appid": key,
    "cnt" :4
}

time_now=datetime.now()
time_hour=time_now.hour


response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
#response=requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=e878e6cdc797a025cf7d709e67c2c963")
response.raise_for_status()
data=response.json()
# print(data)
# print(data["list"][0]["weather"])
# print(data)
# print(os.environ)

weather_ids = [weather['id'] for item in data['list'] for weather in item['weather']]
#print(weather_ids)

for weather_id in weather_ids:
    if weather_id / 100 < 7:
        account_sid = "*****************"
        auth_token = '*******************'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Its going to rain today 😛 in {data['city']['name']}",
            from_='+12138954***',
            to='+1647877****'
        )
        break
