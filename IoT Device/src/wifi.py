import network
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        
        # Wait until connection is established
        while not wlan.isconnected():
            time.sleep(1)
            
    print('Network configuration:', wlan.ifconfig())
    print('Connection successful!')
    
