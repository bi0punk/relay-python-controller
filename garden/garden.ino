#include <SPI.h>
#include <Ethernet.h>

// Definir la dirección MAC y la dirección IP del Arduino
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 177);

EthernetServer server(80);

// Número de relés y pines a los que están conectados
const int numRelays = 4;
int relayPins[] = { 2, 3, 4, 5 };

// Pin analógico para el sensor de humedad
const int moisturePin = A0;

void setup() {
  // Inicializar el servidor Ethernet y los pines de relés
  Ethernet.begin(mac, ip);
  server.begin();
  
  for (int i = 0; i < numRelays; i++) {
    pinMode(relayPins[i], OUTPUT);
    digitalWrite(relayPins[i], HIGH); // Inicialmente apagados
  }
}

void loop() {
  EthernetClient client = server.available();
  
  if (client) {
    // Esperar a que se reciba un comando
    while (!client.available()) {
      delay(1);
    }
    
    // Leer el comando enviado por la aplicación Python
    String command = client.readStringUntil('\r');
    client.flush();
    
    // Procesar el comando y controlar los relés
    if (command.startsWith("on")) {
      int relayNum = command.substring(2).toInt();
      if (relayNum >= 1 && relayNum <= numRelays) {
        digitalWrite(relayPins[relayNum - 1], LOW); // Encender el relé
        client.print("Relay ");
        client.print(relayNum);
        client.println(" encendido");
      } else {
        client.println("Número de relé no válido");
      }
    } else if (command.startsWith("off")) {
      int relayNum = command.substring(3).toInt();
      if (relayNum >= 1 && relayNum <= numRelays) {
        digitalWrite(relayPins[relayNum - 1], HIGH); // Apagar el relé
        client.print("Relay ");
        client.print(relayNum);
        client.println(" apagado");
      } else {
        client.println("Número de relé no válido");
      }
    } else if (command.startsWith("read")) {
      // Leer el valor del sensor de humedad y enviarlo al cliente
      int moistureValue = analogRead(moisturePin);
      client.print("Valor del sensor de humedad: ");
      client.println(moistureValue);
    } else {
      client.println("Comando no válido");
    }
    
    // Cerrar la conexión
    client.stop();
  }
}
