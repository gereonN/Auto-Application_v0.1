from cli_handler import collect_user_input
from webhook_handler import send_data_to_webhook

def main():
    """ Main function to collect user data and send it to the webhook """
    user_data = collect_user_input()
    send_data_to_webhook(user_data)

if __name__ == "__main__":
    main()
