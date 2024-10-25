#!/usr/bin/env python
from confluent_kafka import Consumer, KafkaException, KafkaError
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import json
import time

# example url: localhost:45983
KAFKA_SERVER_URL = 'localhost:29092'
TOPIC = "live_flight_positions_full_france"
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Define the JSON deserializer
def json_deserializer(value):
    if value is None:
        return None
    return json.loads(value.decode('utf-8'))

# Consumer configuration
consumer_conf = {
    'bootstrap.servers': KAFKA_SERVER_URL,
    'group.id': 'live_flight_positions_full_france_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Create a Consumer instance
consumer = Consumer(consumer_conf)

# Subscribe to the topic
consumer.subscribe([TOPIC])

# Connect to your Azure Blob Storage account
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_name = "flightdata"
# Create the container
# container_client = blob_service_client.create_container(container_name)
# time.sleep(10)
# Get a reference to the container
container_client = blob_service_client.get_container_client(container_name)

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            print("Waiting for message...")
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('%% %s [%d] reached end at offset %d\n' %
                      (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Process the received message
            print(f"Received message: key: {msg.key().decode('utf-8')}")
            # Deserialize the JSON message
            data = json_deserializer(msg.value())
            print(f'Received message: data: {data}')
            # Process messages and upload to Azure Blob Storage
            blob_name = f"flight_info_{msg.key().decode('utf-8')}.json"
            blob_client = container_client.get_blob_client(blob=blob_name)
            blob_client.upload_blob(msg.value(), overwrite=False)

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()