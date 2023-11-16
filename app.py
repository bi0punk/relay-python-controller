from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Configura la URL de tu placa Wemos D1
url = "http://192.168.1.115/control"  # Reemplaza con la dirección IP de tu placa

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    command = request.json.get('command')

    if command == 'open':
        response = requests.post(url, data=json.dumps({"command": "open"}), headers={"Content-Type": "application/json"})
        return jsonify(status=response.status_code, message='Bomba de agua abierta')

    elif command == 'close':
        response = requests.post(url, data=json.dumps({"command": "close"}), headers={"Content-Type": "application/json"})
        return jsonify(status=response.status_code, message='Bomba de agua cerrada')

    return jsonify(status=400, message='Comando no válido')

if __name__ == '__main__':
    app.run(debug=True)
