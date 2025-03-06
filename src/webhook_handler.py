import requests
import json

def send_request_to_validate_linkedin(linkedin_profile):
    """ Sendet eine Anfrage an Make zur Validierung der LinkedIn-URL """
    url = "https://hook.eu2.make.com/uhq4dapgnu6dmkwfhbm4mbepw2d6lmdk"
    headers = {"Content-Type": "application/json"}
    payload = {"linkedin_profile": linkedin_profile}

    print(f"🔍 Debug: Sende Anfrage mit Payload: {json.dumps(payload)}")  # Debug-Print

    response = requests.post(url, json=payload, headers=headers)

    print(f"🔍 Debug: Antwort erhalten: {response.text}")  # Debug-Print für die Response

    try:
        return response.json()  # Versuche JSON-Antwort zu parsen
    except json.JSONDecodeError:
        return {"status_code": response.status_code, "error": "Invalid JSON response"}

def send_data_to_webhook(data):
    """ Sendet Daten an den Webhook """
    url = "https://hook.eu2.make.com/uhq4dapgnu6dmkwfhbm4mbepw2d6lmdk"
    headers = {"Content-Type": "application/json"}

    print(f"📡 Debug: Sende Daten an Webhook: {json.dumps(data)}")  # Debug-Print

    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"✅ Debug: Antwort vom Webhook: {response.text}")  # Debug-Print
        response.raise_for_status()  # Fehler auslösen, falls HTTP-Fehler
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Fehler beim Senden: {e}")
        return {"status_code": response.status_code, "error": str(e)}
