# main.py

import sys
print(sys.path)

# Importieren der notwendigen Funktionen aus den jeweiligen Modulen
from src.cli_handler import collect_user_input
from src.webhook_handler import send_request_to_validate_linkedin, send_data_to_webhook

def main():
    """ Hauptfunktion, um Benutzerdaten zu sammeln, das LinkedIn-Profil zu validieren und die Daten an den Webhook zu senden. """

    # Sammeln der Benutzerdaten
    user_data = collect_user_input()

    # Auslesen des LinkedIn-Profils aus den Benutzerdaten
    linkedin_profile = user_data.get('linkedin_profile', '')

    # Überprüfen, ob ein LinkedIn-Profil übergeben wurde
    if linkedin_profile:
        # LinkedIn-Profil validieren
        validation_response = send_request_to_validate_linkedin(linkedin_profile)
        print(f"LinkedIn Validierungsantwort: {validation_response}")
        user_data["linkedin_validation"] = validation_response
    else:
        print("Kein LinkedIn-Profil angegeben!")

    # Sende die gesammelten Benutzerdaten an den Webhook
    send_data_to_webhook(user_data)

if __name__ == "__main__":
    main()
