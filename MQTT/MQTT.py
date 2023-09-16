import paho.mqtt.client as mqtt
import time

# Define MQTT broker information
broker_address = "mqtt.eclipse.org"
broker_port = 1883

# Define your client ID
client_id = "my_mqtt_client"

# Define topics
publish_topic = "my_topic/publish"
subscribe_topic = "my_topic/subscribe"

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(subscribe_topic)

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")

# Create an MQTT client instance
client = mqtt.Client(client_id)

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT loop (this handles network communication)
client.loop_start()

# Publish a message to the topic
message_to_publish = "Hello, MQTT!"
client.publish(publish_topic, message_to_publish)

# Keep the script running to receive messages
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting from MQTT broker...")
    client.disconnect()
    client.loop_stop()
