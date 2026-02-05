from config import CONNECTION_STRING, SEND_INTERVAL_RANGE
from iot_client import IoTClient
from simulator import IoTDeviceSimulator

def main():
    device_client = IoTClient(CONNECTION_STRING)
    simulator = IoTDeviceSimulator(device_client, SEND_INTERVAL_RANGE)
    try:
        device_client.connect()
        simulator.run()
    except KeyboardInterrupt:
        print("Stopping simulation")
    finally:
        device_client.disconnect()
        print("Disconnection Complete")

if __name__ == "__main__":
    main()
