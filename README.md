# relay-python-controller

> Controlador IoT para manejar relés Arduino a través de Flask y TCP sockets. Incluye interfaz web y CLI.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)

## Tabla de Contenidos

- [Características](#características)
- [Stack](#stack)
- [Arquitectura](#arquitectura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Configuración](#configuración)
- [CI](#ci)
- [Limitaciones / Roadmap](#limitaciones--roadmap)
- [Licencia](#licencia)

## Características

- Control de hasta 4 relés desde interfaz web (Flask + HTML/JS)
- CLI interactiva para enviar comandos TCP directamente
- Lectura de sensores (humedad, temperatura) desde el Arduino
- Actualización automática de sensores vía jQuery cada 60 segundos
- Código Arduino incluido (`garden/garden.ino`) para el firmware del microcontrolador
- Comunicación bidireccional mediante sockets TCP

## Stack

- **Python 3.11+**
- **Flask** — servidor web y rutas
- **TCP Sockets** — comunicación con Arduino
- **HTML / jQuery** — interfaz de usuario
- **Arduino** — firmware en C++

## Arquitectura

```
relay-python-controller/
├── .env.example
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── app.py                  # CLI interactiva de comandos TCP
├── main.py                 # Flask web server (placeholder)
├── garden/
│   └── garden.ino          # Firmware para Arduino
├── templates/
│   └── index.html          # UI web de control
└── tests/
    └── test_smoke.py
```

## Requisitos

- Python 3.11 o superior
- Arduino con shield Ethernet/conectividad WiFi
- (Opcional) Flask para la interfaz web

## Instalación

```bash
git clone <repo-url>
cd relay-python-controller
pip install flask
```

## Uso

### CLI interactiva

```bash
python app.py
# Ingrese un comando: on1
# Respuesta del Arduino: OK
# Ingrese un comando: read_temp
```

Comandos disponibles:

| Comando          | Acción                     |
| ---------------- | -------------------------- |
| `on1` / `off1`   | Encender/Apagar relé 1     |
| `on2` / `off2`   | Encender/Apagar relé 2     |
| `on3` / `off3`   | Encender/Apagar relé 3     |
| `read_humidity`  | Leer sensor de humedad     |
| `read_temp`      | Leer sensor de temperatura |
| `read_all`       | Leer todos los sensores    |

### Servidor web

```bash
python main.py
# Abrir http://localhost:5000
```

### Firmware Arduino

Subir `garden/garden.ino` al Arduino y configurar su IP.

## Tests

```bash
pip install pytest ruff
pytest -q
```

## Configuración

Editar `app.py` con la IP del Arduino:

```python
arduino_ip = "192.168.1.177"   # IP de tu Arduino
arduino_port = 80
```

O definir vía variable de entorno (ver `.env.example`):

```
# Environment variables
# Add your configuration here
```

## CI

GitHub Actions — Push/PR:

- `ruff check`
- `pytest`

## Limitaciones / Roadmap

- IP del Arduino hardcodeada en `app.py`
- `main.py` (Flask server) está vacío — pendiente de implementar rutas REST
- Sin autenticación en la interfaz web
- Soporte para un solo Arduino

## Licencia

MIT — ver [LICENSE](LICENSE).
