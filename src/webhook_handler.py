import json
import requests

WEBHOOK_URL = "https://hook.eu2.make.com/uhq4dapgnu6dmkwfhbm4mbepw2d6lmdk"

def send_data_to_webhook(user_data):
    """ Send JSON data to Make.com Webhook """
    response = requests.post(WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(user_data))
    
    if response.status_code == 200:
        print("\n✅ Your application preferences have been successfully sent!")
    else:
        print(f"\n❌ Error sending data! Status Code: {response.status_code}")
        print(response.text)
