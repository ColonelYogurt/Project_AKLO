import paho.mqtt.client as mqtt #import the client1
import time
from csv_mqtt.csv_mqtt import CsvMqtt

# constants
csv_path = "../Assets/Test.csv" 
mqtt_broker = 'mqtt.eclipseprojects.io'
topic = "csv/test" #topic that msg is published to

#connects a client
#client can publish csv files as json
#returns client
def client_connect():
    client = CsvMqtt(mqtt_broker)
    return client

#publishes csv data row by row to topic
#every 5 seconds
def publish_msg(client):
    while True:
        client.publish_csv_data(csv_path, topic)
        time.sleep(5)

if __name__ == "__main__":
    client = client_connect()
    publish_msg(client)