import requests
import os
from dotenv import load_dotenv
import subprocess  # Importer le module subprocess

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration du bot Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CANAL_ID = os.getenv('CANAL_ID')

print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("CHAT_ID:", CHAT_ID)
print("CANAL_ID:", CANAL_ID)

# Fonction pour envoyer un message sur Telegram
def send_to_telegram(message):
    # Utiliser la commande curl pour envoyer un message
    curl_command = f"curl -X POST 'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage' -d 'chat_id={CANAL_ID}&text={message}'"
    print("Executing command:", curl_command)  # Afficher la commande pour déboguer
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)  # Exécuter la commande
    print("Curl output:", result.stdout)  # Afficher la sortie de curl
    print("Curl error (if any):", result.stderr)  # Afficher les erreurs

# Exemple d'information à envoyer
def get_info():
    return "Ceci est un message envoyé à mon canal BABBOOM depuis mon bot Dorpi5_bot."

# Envoi de l'information
if __name__ == '__main__':
    info = get_info()
    response = send_to_telegram(info)
    print(response)  # Affiche la réponse du serveur Telegram
