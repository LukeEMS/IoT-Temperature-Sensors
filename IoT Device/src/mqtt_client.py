import umqtt.simple as mqtt

def connect_to_broker(mqtt_client, broker_endpoint, port, timeout):
    client.connect(broker_endpoint, port, timeout)
    
def create_client(client_id, server):
    return mqtt.MQTTClient(client_id, server)
