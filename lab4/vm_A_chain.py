#Tina Habibi
#Faith Kelin

# https://github.com/koshkatin/EE250-Labs/tree/main

import paho.mqtt.client as mqtt
import time
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("thabibi/pong")
    client.message_callback_add("thabibi/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
    print("Got pong: "+message.payload.decode())

    try:
        pong = int(message.payload.decode())
        ping = pong + 1
        client.publish("thabibi/ping", ping)
        print("Sent ping: ", ping)
    except ValueError:
        print("Message is not an integer")

if __name__ == '__main__':
    #get IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"IP address: {ip_address}") ##added

    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    client.on_message = on_message_from_pong


    client.connect(host="172.20.10.13", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    # Initial ping message
    num = 1
    client.publish("thabibi/ping", num)
    print("Sent initial ping: ", num)

    while True:
        time.sleep(2)