import paho.mqtt.client as mqtt #import the client1
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
topic = "csv/test"

def client_connect():
    client = mqtt.Client("Client_1")
    client.connect(mqtt_broker)

    return client

def publish(client):
    while True:
        client.publish(topic, "just a test")
        print(f"Published to topic: {topic}")
        time.sleep(1)

if __name__ == "__main__":
    client = client_connect()
    publish(client)