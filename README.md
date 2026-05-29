# relay-python-controller

Simple IoT web controller to manage Arduino relays from a Flask web interface. Sends commands over TCP socket to an Arduino board.

## Stack

Python 3, Flask, TCP sockets, Arduino

## Usage

```bash
pip install flask
python app.py
```

Open the web interface and toggle relays on/off. Commands are sent via TCP to the Arduino at the configured IP address.

## License

MIT
