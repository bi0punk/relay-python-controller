#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 177);

EthernetServer server(80);

const int numRelays = 4;
int relayPins[] = { 2, 3, 4, 5 };
const int moisturePin = A0;

void setup() {
  Ethernet.begin(mac, ip);
  server.begin();

  for (int i = 0; i < numRelays; i++) {
    pinMode(relayPins[i], OUTPUT);
    digitalWrite(relayPins[i], HIGH);
  }
}

void loop() {
  EthernetClient client = server.available();

  if (client) {
    while (!client.available()) {
      delay(1);
    }

    String command = client.readStringUntil('\r');
    client.flush();

    if (command.startsWith("on")) {
      int relayNum = command.substring(2).toInt();
      if (relayNum >= 1 && relayNum <= numRelays) {
        digitalWrite(relayPins[relayNum - 1], LOW);
        client.print("Relay ");
        client.print(relayNum);
        client.println(" encendido");
      } else {
        client.println("Número de relé no válido");
      }
    } else if (command.startsWith("off")) {
      int relayNum = command.substring(3).toInt();
      if (relayNum >= 1 && relayNum <= numRelays) {
        digitalWrite(relayPins[relayNum - 1], HIGH);
        client.print("Relay ");
        client.print(relayNum);
        client.println(" apagado");
      } else {
        client.println("Número de relé no válido");
      }
    } else if (command.startsWith("read")) {
      int moistureValue = analogRead(moisturePin);

      // Enviar el valor del sensor de humedad solo como una solicitud POST a la ruta /humidity en el servidor Python
      client.println("POST /humidity HTTP/1.1");
      client.println("Host: 192.168.1.129");  // Cambiar a la dirección correcta del servidor Flask
      client.println("Content-Type: application/x-www-form-urlencoded");
      client.print("Content-Length: ");
      client.println(String("moisture=" + String(moistureValue)).length());
      client.println();
      client.print("moisture=");
      client.println(moistureValue);
    } else {
      client.println("Comando no válido");
    }

    client.stop();
  }
}
