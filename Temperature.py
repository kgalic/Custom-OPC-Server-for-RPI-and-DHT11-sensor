import RPi.GPIO as GPIO
import dht11
import time
import sys
sys.path.insert(0, "..")
import datetime
from opcua import ua, Server


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

server = Server()

print("Server initialized")

url = "opc.tcp://localhost_ip_address:port/freeopcua/server"
server.set_endpoint(url)

print("Endpoint established")

name = "http://example.proof.com"
addSpace = server.register_namespace(name)

print("Namespace registered")


objects = server.get_objects_node()


print("Object node fetched")

values = objects.add_object(addSpace, "Values")
print("Object Value added")

temperature =  values.add_variable(addSpace, "Temperature", 0)
print("Variable Temperature added")

humidity = values.add_variable(addSpace, "Humidity", 0)
print("Variable Humidity added")

temperature.set_writable()
# humidity.set_writeable()
print("All variables writable!")

server.start()

# read data using pin 6
instance = dht11.DHT11(pin=6)
try:
    

    while True:
        result = instance.read()
        if result.is_valid():
            temperature.set_value(result.temperature)
            humidity.set_value(result.humidity)
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)

        time.sleep(1)
finally:
    server.stop()
    print("there was an issue")

