import paho.mqtt.client as mqtt #import the client1
from random import randint
import time

broker = 'mqtt.eclipse.org'
port = 1883
topic = "python/mqtt/test"
client_id = f'python-mqtt-{randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


broker_address="localhost" #From example code
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

broker_address="localhost"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","Connection/confirmation/confirm1")
client.subscribe("Connection/confirmation/confirm1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("Connection/confirmation/confirm1","connection")


#Receiving
client.on_message=on_message        #attach function to callback
client.loop_start()    #start the loop
