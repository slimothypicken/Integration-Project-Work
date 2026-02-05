import time
import random
from telemetry import telemetry_data_generator, battery_voltage_alert

class IoTDeviceSimulator:
    def __init__(self, client, interval_range):
        self.client = client
        self.interval_range = interval_range

    def run(self):
        while True:
            telemetry =  telemetry_data_generator()
            alert = battery_voltage_alert(telemetry["battery_voltage"])

            self.client.send_message(telemetry, alert)

            time.sleep(random.randint(*self.interval_range))
