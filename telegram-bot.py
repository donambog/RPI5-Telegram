import requests
import os
from dotenv import load_dotenv
import subprocess  # Import subprocess module

# Load environment variables from the .env file
load_dotenv()

# Telegram bot configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CANAL_ID = os.getenv('CANAL_ID')

print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("CHAT_ID:", CHAT_ID)
print("CANAL_ID:", CANAL_ID)

# Function to send a message to Telegram
def send_to_telegram(message):
    # Use curl command to send a message
    curl_command = f"curl -X POST 'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage' -d 'chat_id={CANAL_ID}&text={message}'"
    print("Executing command:", curl_command)  # Print command for debugging
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)  # Execute command
    print("Curl output:", result.stdout)  # Print curl output
    print("Curl error (if any):", result.stderr)  # Print errors if any

# Example information to send
def get_info():
    return "This is a message sent to my channel BABBOOM from my bot Dorpi5_bot."

# Send the information
if __name__ == '__main__':
    info = get_info()
    response = send_to_telegram(info)
    print(response)  # Print server response from Telegram

