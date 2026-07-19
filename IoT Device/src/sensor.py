# Red = 3.3v, Yellow = Data, White = Ground
import onewire, ds18x20, time
from machine import Pin
def find_sensors(data_pin, sensor_index):
    # Set the data pin for the sensor
    SensorPin = Pin(data_pin, Pin.IN)
    # Tell MicroPython we're using a DS18B20 sensor, and which pin it's on
    sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
    # Look for DS18B20 sensors (each contains a unique rom code)
    roms = sensor.scan()
    
    return sensor,roms[sensor_index]

def get_temperature_value(sensor, rom):
    sensor.convert_temp() # Convert the sensor units to centigrade
    time.sleep(1)
    return sensor.read_temp(rom)