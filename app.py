import requests

while True:
    command = input("Ingrese el comando (e.g., open1, close2) o 'q' para salir: ")
    if command.lower() == 'q':
        break
    
    url = f"http://direccion_ip_de_tu_wemos/command?command={command}"
    response = requests.get(url)
    
    print(f"Respuesta del servidor: {response.text}")
