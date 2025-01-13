import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OMW_API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


weather_params = {
    "lat": 40.640064,
    "lon": 22.944420,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
question_data = weather_data
print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Its going to rain bring an ubrella !!!',
        to='whatsapp:+306944812123'
    )

    print(message.status)

