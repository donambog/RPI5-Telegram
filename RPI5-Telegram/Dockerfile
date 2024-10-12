# Utiliser une image de base Python
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier le fichier requirements.txt et le script python dans le conteneur
COPY requirements.txt ./
COPY telegram-bot.py ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour exécuter votre script
CMD ["python", "./telegram-bot.py"]

