import os
import socket
import logging
from flask import Flask, render_template, request, jsonify, abort
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

ARDUINO_IP = os.environ.get("ARDUINO_IP", "192.168.1.177")
ARDUINO_PORT = int(os.environ.get("ARDUINO_PORT", "80"))
API_TOKEN = os.environ.get("API_TOKEN")

ALLOWED_COMMANDS = {
    "on1", "off1", "on2", "off2", "on3", "off3",
    "read_humidity", "read_temp", "read_all"
}


def require_auth():
    token = request.headers.get("X-API-Token")
    if not token or token != API_TOKEN:
        abort(401, description="Unauthorized")


def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ARDUINO_IP, ARDUINO_PORT))
            s.sendall(command.encode())
            data = s.recv(1024)
        return data.decode()
    except socket.timeout:
        app.logger.error("Timeout connecting to Arduino at %s:%s", ARDUINO_IP, ARDUINO_PORT)
        return None
    except Exception as e:
        app.logger.error("Arduino connection failed: %s", e)
        return None


@app.route("/")
def index():
    return render_template("index.html", commands=sorted(ALLOWED_COMMANDS), api_token=API_TOKEN or "")


@app.route("/api/command", methods=["POST"])
def command():
    require_auth()
    data = request.json
    cmd = data.get("command", "").lower()
    if cmd not in ALLOWED_COMMANDS:
        return jsonify({"error": f"Comando no válido. Permitidos: {', '.join(sorted(ALLOWED_COMMANDS))}"}), 400
    response = send_command(cmd)
    if response is None:
        return jsonify({"error": "No se pudo conectar con el Arduino"}), 502
    return jsonify({"command": cmd, "response": response})


@app.route("/api/status", methods=["GET"])
def status():
    require_auth()
    response = send_command("read_all")
    if response is None:
        return jsonify({"error": "No se pudo conectar con el Arduino"}), 502
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
