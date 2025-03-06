import requests
import json

def send_request_to_validate_linkedin(linkedin_profile):
    """Send a request to validate the LinkedIn profile through the webhook."""
    
    # URL des Webhooks (ersetze dies mit deiner tatsächlichen Webhook-URL)
    url = "https://hook.eu2.make.com/your-webhook-url"  
    headers = {
        "Content-Type": "application/json"
    }
    
    # Daten, die im Request gesendet werden
    payload = {
        "linkedin_profile": linkedin_profile
    }
    
    try:
        # Senden einer POST-Anfrage an den Webhook
        response = requests.post(url, json=payload, headers=headers)
        
        # Wenn der Statuscode 200 ist, geben wir die Antwort als JSON zurück
        if response.status_code == 200:
            return response.json()  # Gibt die Antwort des Webhooks zurück
        else:
            # Wenn ein Fehler auftritt, geben wir den Statuscode und eine Nachricht zurück
            return {"status_code": response.status_code, "message": "Error with LinkedIn profile validation"}
    
    except requests.exceptions.RequestException as e:
        # Falls ein Fehler bei der Anfrage auftritt, fangen wir ihn hier ab
        return {"status_code": 500, "message": str(e)}
