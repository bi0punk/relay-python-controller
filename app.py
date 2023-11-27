import socket
import time

# Dirección IP y puerto del Arduino
arduino_ip = "192.168.1.177"
arduino_port = 80

# Función para enviar comandos al Arduino
def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((arduino_ip, arduino_port))
        s.sendall(command.encode())
        data = s.recv(1024)
    print("Respuesta del Arduino:", data.decode())

# Enviar comandos al Arduino (puedes ajustar estos comandos según tus necesidades)
send_command("on1")
time.sleep(2)  # Esperar 2 segundos
send_command("off1")
