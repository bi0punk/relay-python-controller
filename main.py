from flask import Flask, request, jsonify, render_template
import socket

app = Flask(__name__)

# Dirección IP y puerto del Arduino
arduino_ip = "192.168.1.177"
arduino_port = 80

# Función para enviar comandos al Arduino
def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((arduino_ip, arduino_port))
        s.sendall(command.encode())
        data = s.recv(1024)
    return data.decode()

# Ruta para la interfaz web
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir datos de humedad (POST)
@app.route('/humidity', methods=['POST'])
def humidity():
    humidity_value = request.form['moisture']
    # Puedes realizar acciones con el valor de humedad recibido, si es necesario
    print("Valor de humedad recibido: {}".format(humidity_value))
    return "OK"

# Ruta para obtener datos de humedad (GET)
@app.route('/get_humidity', methods=['GET'])
def get_humidity_data():
    humidity_data = get_humidity()
    return jsonify({"humidity": humidity_data})

# Ruta para enviar comandos al Arduino (POST)
@app.route('/command', methods=['POST'])
def command():
    command = request.form['command']
    if command == "read_humidity":
        response = get_humidity()
    else:
        response = send_command(command)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(host="192.168.1.129")
