import requests

while True:
    command = input("Ingrese el comando (e.g., open1, close2) o 'q' para salir: ")
    if command.lower() == 'q':
        break
    
    url = f"http://192.168.1.115/command?command={command}"
    response = requests.get(url)
    
    print(f"Respuesta del servidor: {response.text}")
