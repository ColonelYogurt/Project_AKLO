import paho.mqtt.client as mqtt #import the client1

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


broker_address="192.168.1.184" #From example code

client = mqtt.Client("P1") #create new instance

client.on_message=on_message

client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF")#publish