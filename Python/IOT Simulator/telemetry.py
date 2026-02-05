import random
import time

def telemetry_data_generator():
    return{
        "timestamp": time.time(),
        "battery_voltage":  5 + (random.random() * 15),
        "operating_hours":  1 + (random.random() * 240),
        "engine_speed":  250 + (random.random() * 1500),
        }
       
def battery_voltage_alert(battery_voltage) -> bool:
    return battery_voltage > 20
