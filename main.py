import requests
import os

PARAMETER = {"lat":18.631451 , "lon":73.797081, "appid": os.environ['API_KEY'],  "exclude":"current,minutely,daily"}

request_url = requests.get(url= "https://api.openweathermap.org/data/2.5/onecall",params=PARAMETER,)

request_url.raise_for_status()
data = request_url.json()
list1 = []
hourly = data["hourly"][:12]
for n in range(0,12):
    hcbhole = hourly[n]["weather"][0]["id"]
    list1.insert(n,hcbhole)


willRain = False

for m in list1:
    if m < 700:
        willRain = True

if willRain:

    import os
    from twilio.rest import Client

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Today will rain, Don't Forgot to keep Umbrella (☂) 😊.",
        from_='phone number get from Twilio site',
        to='Verified phone number on which we have to send message'
    )

    print(message.sid)
