import paho.mqtt.client as mqtt #import the client1
from random import randint

broker = 'mqtt.eclipse.org'
port = 1883
topic = "python/mqtt/test"
client_id = f'python-mqtt-{randint(0, 1000)}'

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

broker_address="localhost"
print("creating new instance")

client = mqtt.Client("P1") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Subscribing to topic","Connection/confirmation/confirm1")
client.subscribe("Connection/confirmation/confirm1")

print("Publishing message to topic","house/bulbs/bulb1")
client.publish("Connection/confirmation/confirm2","connection")


#Receiving
client.on_message=on_message        #attach function to callback
client.loop_start()    #start the loop