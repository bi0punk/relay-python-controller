from flask import Flask, render_template, request
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

# Rutas para la interfaz web
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    command = request.form['command']
    response = send_command(command)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
