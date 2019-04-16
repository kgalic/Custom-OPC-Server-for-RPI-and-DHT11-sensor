# Custom-OPC-Server-for-RPI-and-DHT11-sensor
This project contains a code sample of OPC-UA Server(based on freeOPCUA) that reads data from DHT11 sensor and publishes these values to the specific nodes

# Free OPC UA:
  https://github.com/FreeOpcUa/python-opcua

# Installation

With pip (note: the package was ealier called freeopcua)

    pip install opcua

Ubuntu:

    apt install python-opcua        # Library
    apt install python-opcua-tools  # Command-line tools

Dependencies:
* Python > 3.4: `cryptography`, `dateutil`, `lxml` and `pytz`. 
* Python 2.7 or pypy < 3: you also need to install `enum34`, `trollius` (`asyncio`), and `futures` (`concurrent.futures`),
  with pip for example.

# DHT11 Python library:
  https://github.com/szazo/DHT11_Python