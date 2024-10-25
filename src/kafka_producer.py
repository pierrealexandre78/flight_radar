from confluent_kafka import Producer
import json

KAFKA_SERVER_URL = 'localhost:29092'
# Define the topic
TOPIC = "live_flight_positions_full_france"

# Define the examplemessage
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

# Producer configuration
producer_conf = {
    'bootstrap.servers': KAFKA_SERVER_URL
}

# Create a Producer instance
producer = Producer(producer_conf)

# Define the delivery report callback function
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
    print('Message content: {}'.format(msg.value().decode('utf-8')))

# load test data
with open('data/live_flight_positions_full_france.json', 'r') as f:
    json_live_flight_positions_full_france = json.load(f)['data']

# split data into single flight info message
for count, flight_info_message in enumerate(json_live_flight_positions_full_france):
    # Produce the message
    producer.produce(TOPIC,
                     key=flight_info_message['fr24_id'].encode('utf-8'),
                     value=json.dumps(flight_info_message).encode('utf-8'),
                     callback=delivery_report)

# Wait for any outstanding messages to be delivered
producer.flush()