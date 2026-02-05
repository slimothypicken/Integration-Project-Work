import json
from azure.iot.device import IoTHubDeviceClient, Message


class IoTClient:
    def __init__(self, connection_string):
        self.client = IoTHubDeviceClient.create_from_connection_string(connection_string)
       
    def connect(self):
        self.client.connect()
    def disconnect(self):
        self.client.disconnect()
    def send_message(self, telemetry, alert: bool):
        message = Message(json.dumps(telemetry))
        message.content_encoding = "utf-8"
        message.content_type = "application/json"
        message.custom_properties["batteryVoltageAlert"] = str(alert).lower()

        self.client.send_message(message)