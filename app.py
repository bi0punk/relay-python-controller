import requests
import json

# Configura la URL de tu placa Wemos D1
url = "http://192.168.1.112/control"  # Reemplaza con la dirección IP de tu placa

# Define los códigos ANSI para colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
while True:
    # Solicitar al usuario ingresar el comando
    user_input = input("Ingrese el comando (open/close/exit): ").strip().lower()

    if user_input == "open":
        # Enviar el comando para abrir la bomba
        response = requests.post(url, data=json.dumps({"command": "open"}), headers={"Content-Type": "application/json"})

        # Verificar la respuesta del servidor
        if response.status_code == 200:
            print(GREEN + "Bomba de agua abierta" + RESET)
        else:
            print(RED + "Error en la solicitud" + RESET)

    elif user_input == "close":
        # Enviar el comando para cerrar la bomba
        response = requests.post(url, data=json.dumps({"command": "close"}), headers={"Content-Type": "application/json"})

        # Verificar la respuesta del servidor
        if response.status_code == 200:
            print(RED + "Bomba de agua cerrada" + RESET)
        else:
            print(RED + "Error en la solicitud" + RESET)

    elif user_input == "exit":
        break  # Salir del bucle si el usuario ingresa "exit"

    else:
        print("Comando no válido. Ingrese 'open', 'close' o 'exit'.")
