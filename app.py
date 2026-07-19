import os
import socket
from dotenv import load_dotenv

load_dotenv()

arduino_ip = os.environ.get("ARDUINO_IP", "192.168.1.177")
arduino_port = int(os.environ.get("ARDUINO_PORT", "80"))

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((arduino_ip, arduino_port))
            s.sendall(command.encode())
            data = s.recv(1024)
        print("Respuesta del Arduino:", data.decode())
    except socket.timeout:
        print("Error: Timeout conectando al Arduino")
    except Exception as e:
        print(f"Error: {e}")

ALLOWED_COMMANDS = {"on1", "off1", "on2", "off2", "on3", "off3", "read_humidity", "read_temp", "read_all"}

if __name__ == "__main__":
    while True:
        user_input = input("Ingrese un comando (o 'exit' para salir): ")
        if user_input.lower() == 'exit':
            break
        if user_input.lower() not in ALLOWED_COMMANDS:
            print(f"Comando no válido. Permitidos: {', '.join(sorted(ALLOWED_COMMANDS))}")
            continue
        send_command(user_input)
