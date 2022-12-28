import paho.mqtt.client as mqtt #import the client1
from random import randint
import csv 
import time

broker = 'mqtt.eclipse.org'
port = 1883
topic = "python/mqtt/test"
client_id = f'python-mqtt-{randint(0, 1000)}'

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to server")
        client.publish("Connection/confirmation/confirm1", "connect")
    else:
        print("Failed to connect to server")
        

def on_disconnect(client, userdata, flags, rc=0):
    print("DIsconnected "+str(rc))

def on_message(client, userdata, message):
    topic = message.topic
    message_new = str(message.payload.decode("utf-8", "ignore"))
    print("message: ", message_new)

broker_address="localhost"
print("creating new instance")

client = mqtt.Client("P1") #create new instance

client.on_log = on_log
client.on_disconnect=on_disconnect
client.on_connect = on_connect
client.on_message=on_message

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start()    #start the loop

client.subscribe("data/file")
client.publish("data/file", "Test.csv")

myfile = open("Assets/Test.csv", 'r')
Lines = myfile.readlines()
for line in Lines:
  client.publish("test/filereading", line[0])

client.loop_stop()

client.publish("Connection/confirmation/confirm1", "disconnect")
client.disconnect()
