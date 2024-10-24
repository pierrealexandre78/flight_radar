# Apache Kafka - Live Flight Data streaming

Technology used: *Azure (VM, Blob Storage, Azure Functions, Azure Devops, Azure Data Lake Analytics, Azure Synapse), Kafka, Spark, python*

## Abstract

The goal of the project was to get to know how Apache Kafka streams works. For training purposes, I used an Azure free B1s machine and simulated the stream of the data to avoid memory problems on the Azure instance. Each event in the simulated streaming was created as a sample JSON file from an existing dataset. The streamed data was uploaded to an Azure Blob Storage and analyzed by a Data Factory, which created a table schema in the Azure Data Lake Analytics. That allowed me to perform queries in Azure Synapse Analytics.

## Installation

### Pre-requisite:
* active Azure account subscription

### Kafka server setup
Setup Kafka server on Azure VM:

1. Creating a free Azure instance B1s and running it using secure shell.

2. install and start Docker Engine . Verify that Docker is set up properly by ensuring that no errors are output when you run docker info in your terminal.

3. Kafka Confluent setup
#### Install kafka
```bash
make install_kafka
```
#### Start the kafka server
```bash
confluent local kafka start
```

#### Create the topic: live flight position 
```bash
confluent local kafka topic create live_flight_positions_full_france
```

4. Run the producer on another shell.

5. Run the consumer on another shell.


