# Imports
import time
import src.sensor as s
import src.mqtt_client as mqtt
import src.wifi as wifi
import json

with open('config.json') as f:
    config_settings = json.load(f)
    
wifi.connect_wifi(config_settings["ssid"],config_settings["ssid_password"])
 
sensor, rom = s.find_sensors(0,0)
 
mqtt_client = mqtt.create_client(1,config_settings["mqtt_broker"])

while True: # Run forever
 
    print(f"Temp: {s.get_temperature_value(sensor, rom)}")
    mqtt_client.publish("room1/air/temperature",s.get_temperature_value(sensor, rom))
    
    time.sleep(1)
    