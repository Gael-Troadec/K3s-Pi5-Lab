from flask import Flask
import platform
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return f"SYSTEM ARCHITEUTHIS ONLINE\npod ID: {socket.gethostname()}\nArchitecture: {platform.machine()}\n"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    print("Demarrage du Serveur Web Architeuthis...", flush=True)
    app.run(host='0.0.0.0', port=5000)