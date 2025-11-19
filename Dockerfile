# On part d'une image legere officielle
FROM python:3.11-slim
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]