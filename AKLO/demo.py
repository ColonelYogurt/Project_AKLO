import paho.mqtt.client as mqtt #import the client1
from random import randint
import csv 
import time

broker = 'mqtt.eclipse.org'
port = 1883
topic = "python/mqtt/test"
client_id = f'python-mqtt-{randint(0, 1000)}'



# Updates file with new information
def edit_file(new_message, pos):

    #Takes new_messange (in row form) and seperates values
    mess_elem = new_message.split(",")
    file_list = []

    # Declares local objects
    in_file = open("Assets/Test.csv", "r")
    reader = csv.reader(in_file)
    
    #Rips file and re-assembles as needed
    for row in reader:
        #Alters information as needed
        if row[0] == mess_elem[0]:
            row[pos] = mess_elem[1]
        #writer.writerow(row)
        file_list.append(row)

    out_file = open("Assets/Test.csv", "w")
    writer = csv.writer(out_file)
    for row in file_list:
        writer.writerow[row]

    in_file.close()    
    out_file.close()

def on_log(client, userdata, level, buf):
    print("log: " + buf)

#establishes and confirms connection
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to server")
        client.publish("Connection/confirmation/confirm1", "connected")
    else:
        print("Failed to connect to server")
        
#Executes diconnection protocol
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected "+str(rc))

#Detects and triggers on information to update
def on_message(client, userdata, message):
    topic = message.topic

    if topic == "Interaction/sensor/console2":
        message_new = str(message.payload.decode("utf-8", "ignore"))
        edit_file(message_new, 10)

    elif topic == "Interaction/transducer/console2":
        message_new = str(message.payload.decode("utf-8", "ignore"))
        edit_file(message_new, 11)

    return(message_new)

def send_new(client, info, topic):   
    
    if topic == "Interaction/sensor/console2":
        client.publish("Interaction/sensor/console2", info)
    
    elif topic == "Interaction/transducer/console2":
        client.publish("Interaction/transducer/console2", info)
    

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
client.subscribe("Interaction/sensor/console2")
client.subscribe("Interaction/transducer/console2")

#Rips file and re-assembles as needed
sensor_topic = "Interaction/sensor/console2"
transdeuser_topic = "Interaction/transducer/console2"

# Declares local objects
with open("Assets/Test.csv", "r") as local_file:
    temp_reader = csv.reader(local_file)

    for row in temp_reader:
        send_new(client, "hello", sensor_topic)
        send_new(client, "hello", transdeuser_topic)

    local_file.close() 

client.subscribe("data/file")
client.publish("data/file", "Test.csv")

client.loop_stop()

client.publish("Connection/confirmation/confirm1", "disconnect")
client.disconnect()