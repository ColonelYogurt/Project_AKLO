import paho.mqtt.client as mqtt #import the client1
from random import randint
import csv 
import time

broker = 'mqtt.eclipse.org'
port = 1883
topic = "python/mqtt/test"
client_id = f'python-mqtt-{randint(0, 1000)}'



def edit_file(new_message, pos):

    mess_elem = new_message.split(",")
    in_file = open("Assets/Test.csv", "rb")
    reader = csv.reader(in_file)
    out_file = open("Assets/Test.csv", "wb")
    writer = csv.writer(out_file)

    for row in reader:
        if row[0] == mess_elem[0]:
            row[pos] = mess_elem[1]
            writer.writerow(row)

    in_file.close()    
    out_file.close()

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to server")
        client.publish("Connection/confirmation/confirm1", "connected")
    else:
        print("Failed to connect to server")
        

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected "+str(rc))

def on_message(client, userdata, message):
    topic = message.topic

    if topic == "Interaction/sensor/console2":
        message_new = str(message.payload.decode("utf-8", "ignore"))
        edit_file(message_new, 10)

    elif topic == "Interaction/Transdueser/console2":
        message_new = str(message.payload.decode("utf-8", "ignore"))
        edit_file(message_new, 11)

    return(message_new)

def send_new(client, info, topic):
    if topic == "Interaction/sensor/console2":
        client.publish("Interaction/sensor/console2", info)
        #Writes into csv file will complete on 12/28/2022

    elif topic == "Interaction/Transdueser/console2":
        client.publish("Interaction/Transdueser/console2", info)
    

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

#Requires further definition needs to be discussed

client.subscribe("data/file")
client.publish("data/file", "Test.csv")

client.loop_stop()

client.publish("Connection/confirmation/confirm1", "disconnect")
client.disconnect()