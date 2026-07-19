import requests
import os

token = os.environ.get("LICHESS_BOT_TOKEN")
headers = {"Authorization": f"Bearer {token}"}
response = requests.post("https://lichess.org/api/bot/account/upgrade", headers=headers)

print("STATUS CODE:", response.status_code)
print("RESPONSE:", response.text
     )
