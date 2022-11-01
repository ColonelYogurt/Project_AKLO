import time
import paho.mqtt.client as mqtt

mqtt_broker = 'mqtt.eclipseprojects.io'
topic = "csv/test"

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

def client_connect():
    client = mqtt.Client("Client_2")
    client.connect(mqtt_broker)

    return client

def subscribe(client):

    client.loop_start()

    client.subscribe(topic)
    client.on_message=on_message

    time.sleep(5)

    client.loop_stop()

if __name__ == "__main__":
    client = client_connect()
    subscribe(client)