from flask import Flask, request, render_template
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

# Ruta para enviar comandos al Arduino (POST)
@app.route('/command', methods=['POST'])
def command():
    command = request.form['command']
    if command.startswith("on") or command.startswith("off"):
        response = send_command(command)
    else:
        response = "Comando no válido"
    return response

# Ruta para recibir datos de humedad (POST)
@app.route('/humidity', methods=['POST'])
def humidity():
    humidity_value = request.data.decode('utf-8')
    # Puedes realizar acciones con el valor de humedad recibido, si es necesario
    print("Valor de humedad recibido: {}".format(humidity_value))
    return "OK"

if __name__ == '__main__':
    app.run()
