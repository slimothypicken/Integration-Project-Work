import os

CONNECTION_STRING = os.environ.get("AZURE_IOT_CONNECTION")

if not CONNECTION_STRING:
    raise ValueError("Environment variable 'AZURE_IOT_CONNECTION' is not set.")

SEND_INTERVAL_RANGE = (3,10)  # seconds