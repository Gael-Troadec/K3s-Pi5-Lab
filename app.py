from flask import Flask
import platform
import socket
import redis
import os

app = Flask(__name__)

redis_password = os.getenv('REDIS_PASSWORD')

db = redis.Redis(host='redis-service', port=6379, password=redis_password, decode_responses=True)

@app.route('/')
def hello():
    try:
        count = db.incr('hits')
        redis_status = "CONNECTED"
    except redis.ConnectionError:
        count = "ERROR"
        redis_status = "DISCONNECTED (Auth Failed?)"

    return (f"SYSTEM ARCHITEUTHIS ONLINE\n"
            f"Version: v2.0 (CI/CD Automated)\n"
            f"Pod ID: {socket.gethostname()}\n"
            f"Architecture: {platform.machine()}\n"
            f"Memory State (Redis): {redis_status}\n"
            f"Number of persistent visits: {count}\n")

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    print("Demarrage du Serveur Web Architeuthis...", flush=True)
    app.run(host='0.0.0.0', port=5000)