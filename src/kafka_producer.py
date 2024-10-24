import time
import json
from random import choice
from confluent_kafka import Producer
import os 

# example url: localhost:45983
KAFKA_SERVER_URL = os.environ.get('KAFKA_SERVER_URL')
TOPIC = "live_flight_positions_full_france"

if __name__ == '__main__':

    config = {
        # User-specific properties : local env here
        'bootstrap.servers': KAFKA_SERVER_URL,

        # Fixed properties
        'acks': 'all'
    }

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))



    with open('data/live_flight_positions_full_france.json', 'r') as f:
        json_live_flight_positions_full_france = json.load(f)['data']

    flight_numbers_list = []
    destinations_list = []
    for count, single_flight_info in enumerate(json_live_flight_positions_full_france):
        if single_flight_info['callsign'] is not None:
            flight_numbers_list.append(single_flight_info['callsign'])
        if single_flight_info['dest_iata'] is not None:
            destinations_list.append(single_flight_info['dest_iata'])

    # Produce data by selecting random values from these lists.
    count = 0
    for _ in range(10):
        flight_number= choice(flight_numbers_list)
        destination = choice(destinations_list)
        producer.produce(TOPIC,destination, flight_number, callback=delivery_callback)
        count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()