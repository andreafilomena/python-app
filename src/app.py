# Importing flask module in the project
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({"time": datetime.datetime.now().isoformat(), "hostname": socket.gethostname()}), 200

@app.route('/api/v1/healthz')
def health():
    return jsonify({"status": "up"}), 200

if __name__ == '__main__':
    app.run()