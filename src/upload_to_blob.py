import json
import os
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

class Message:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# test data to upload
example_message = {
    "fr24_id": "37acbb1e",
    "flight": "SKV112",
    "callsign": "SKV112",
    "lat": 50.89319,
    "lon": 3.73833,
    "track": 106,
    "alt": 41000,
    "gspeed": 460,
    "vspeed": -64,
    "squawk": "5242",
    "timestamp": "2024-10-23T15:00:33Z",
    "source": "ADSB",
    "hex": "4401DA",
    "type": "F2TH",
    "reg": "OE-HHS",
    "painted_as": "SKV",
    "operating_as": "SKV",
    "orig_iata": "LTN",
    "orig_icao": "EGGW",
    "dest_iata": "LCA",
    "dest_icao": "LCLK",
    "eta": "2024-10-23T18:40:57Z"
}

# Connect to your Azure Blob Storage account
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_name = "testflightdata"
# Create the container
container_client = blob_service_client.create_container(container_name)
time.sleep(10)
container_client = blob_service_client.get_container_client(container_name)

message = Message(example_message['fr24_id'], example_message)

# Process messages and upload to Azure Blob Storage
blob_name = f"flight_info_{message.key}_{message.value['timestamp']}.json"
blob_client = container_client.get_blob_client(blob=blob_name)
blob_client.upload_blob(json.dumps(message.value), overwrite=False)