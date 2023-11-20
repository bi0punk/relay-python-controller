from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Configura la URL de tu placa Wemos D1
url = "http://192.168.1.112/control"  # Reemplaza con la dirección IP de tu placa

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command():
    user_input = request.form['command'].strip().lower()

    if user_input in ["open", "close"]:
        relay_number = user_input[-1]  # Obtén el número de relé del comando
        response = requests.post(url, data=json.dumps({"command": user_input + relay_number}), headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            return "Bomba de agua " + ("abierta" if user_input == "open" else "cerrada")
        else:
            return "Error en la solicitud"

    elif user_input == "exit":
        return "Exiting..."

    else:
        return "Comando no válido. Ingrese 'open', 'close' o 'exit'."

if __name__ == '__main__':
    app.run(debug=True)
