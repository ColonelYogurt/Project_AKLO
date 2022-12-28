import re
import paho.mqtt.client as mqtt
import json

#constants
mqtt_broker = 'mqtt.eclipseprojects.io'
topic = "csv/test"

#connects a client as a Client object
#returns that client
def connect_mqtt():
    client = mqtt.Client()
    client.connect(mqtt_broker, 1883, 60)
    return client

#function that runs when client connects to broker
def on_connect(client, userdata, flags, rc):
    print("Successfully connected with result code "+str(rc))
    client.subscribe(topic)

#function that runs when message is received
#outputs sensor and transducer data
def on_message(client, userdata, msg):

    #receives payload
    res = msg.payload
    final_res = json.loads(res.decode('utf-8')) #converts payload to json

    print("Sensor: ", final_res["Sensor"])
    print("Transducer: ", final_res["Transducer"])

if __name__ == "__main__":
    client = connect_mqtt()

    client.on_connect = on_connect #function passed into client
    client.on_message = on_message #function passed into client

    client.loop_forever()