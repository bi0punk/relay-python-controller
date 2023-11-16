from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

# Configura la URL de tu placa Wemos D1
url = "http://192.168.1.115/control"  # Reemplaza con la dirección IP de tu placa

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    command = request.form.get('command')  # Cambia a request.form para obtener datos de formulario

    if command in ['open1', 'close1', 'open2', 'close2', 'open3', 'close3', 'open4', 'close4']:
        response = requests.post(url, data={'command': command})
        relay_number = command[-1]  # Obtén el número de relé del comando
        return jsonify(status=response.status_code, message=f'Relé {relay_number} {command[:-1]}ado')

    return jsonify(status=400, message='Comando no válido')

if __name__ == '__main__':
    app.run(debug=True)
