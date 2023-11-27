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

# Loop para ingresar comandos desde el teclado
while True:
    user_input = input("Ingrese un comando (o 'exit' para salir): ")
    
    if user_input.lower() == 'exit':
        break
    
    send_command(user_input)
