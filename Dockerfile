FROM python:3.11-slim
ENV PYTHONBUFFERED=1
WORKDIR /app
RUN pip install flask
COPY app.py .
CMD ["python", "app.py"]