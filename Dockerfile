# On part d'une image legere officielle
FROM python:3.11-slim

# Repertoire de travail dans le conteneur
WORKDIR /app

# Copie du code source
COPY app.py .

# Commande de lancement
CMD ["python", "app.py"]