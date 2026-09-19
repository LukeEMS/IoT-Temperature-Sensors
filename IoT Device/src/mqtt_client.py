import umqtt.simple as mqtt

def create_client(client_id, server, port):
    return mqtt.MQTTClient(client_id, server, port)
