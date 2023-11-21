#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "nombre_de_tu_wifi";
const char* password = "contraseña_de_tu_wifi";

ESP8266WebServer server(80);

const int relayPin[] = {D1, D2, D3, D4};  // Pines de los relés

void handleCommand() {
  String command = server.arg("command");

  // Analizar el comando recibido
  if (command.startsWith("open") || command.startsWith("close")) {
    int relayNum = command.substring(4).toInt();
    if (relayNum >= 1 && relayNum <= 4) {
      int state = (command.startsWith("open")) ? LOW : HIGH;
      digitalWrite(relayPin[relayNum - 1], state);  // Cambiar el estado del relé
      server.send(200, "text/plain", "Comando recibido: " + command);
      return;
    }
  }

  server.send(400, "text/plain", "Comando no válido");
}

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 4; i++) {
    pinMode(relayPin[i], OUTPUT);
    digitalWrite(relayPin[i], HIGH);  // Inicialmente apagar todos los relés
  }

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando al WiFi...");
  }
  Serial.println("Conectado al WiFi");

  server.on("/command", HTTP_GET, handleCommand);

  server.begin();
  Serial.println("Servidor iniciado");
}

void loop() {
  server.handleClient();
}
