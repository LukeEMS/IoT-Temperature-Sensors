import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def connect_to_broker(mqtt_client, broker_endpoint, port, timeout):
    client.connect(broker_endpoint, port, timeout)
    
    
def create_client(callback_api_version = mqtt.CallbackAPIVersion.VERSION2):
    return mqtt.Client(callback_api_version)