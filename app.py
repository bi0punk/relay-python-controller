import socket

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

ALLOWED_COMMANDS = {"on1", "off1", "on2", "off2", "on3", "off3", "read_humidity", "read_temp", "read_all"}

while True:
    user_input = input("Ingrese un comando (o 'exit' para salir): ")
    
    if user_input.lower() == 'exit':
        break
    
    if user_input.lower() not in ALLOWED_COMMANDS:
        print(f"Comando no válido. Permitidos: {', '.join(sorted(ALLOWED_COMMANDS))}")
        continue
    
    send_command(user_input)
