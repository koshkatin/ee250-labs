#Tina Habibi
#Faith Klein

# https://github.com/koshkatin/EE250-Labs/tree/main

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to server (i.e., broker) with result code "+str(reason_code))

    client.subscribe("thabibi/ping")
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("thabibi/ping", on_message_from_ping)


def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_ping(client, userdata, message):
   print("Got ping: "+message.payload.decode())
   
   # convert the message to an integer
   try:
       ping = int(message.payload.decode())
       pong = ping + 1
       client.publish("thabibi/pong", pong)
       print("Sent pong: ", pong)
   except ValueError:
        print("Message is not an integer")




if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect


    client.connect(host="172.20.10.13", port=1883, keepalive=60)

    client.loop_forever()