# Apache Kafka - Live Flight Data streaming

Technology used: *Azure (VM, Blob Storage, Azure Functions, Azure Devops, Azure Data Lake Analytics, Azure Synapse), Kafka, Spark, python*

## Abstract

The goal of the project was to get to know how Apache Kafka streams works. For training purposes, I used an Azure free B1s machine and simulated the stream of the data to avoid memory problems on the Azure instance. Each event in the simulated streaming was created as a sample JSON file from an existing dataset. The streamed data was uploaded to an Azure Blob Storage and analyzed by a Data Factory, which created a table schema in the Azure Data Lake Analytics. That allowed me to perform queries in Azure Synapse Analytics.

## Installation

### Pre-requisite:
* active Azure account subscription

### Kafka server setup
Setup Kafka server on Azure VM:

1. Create a VM instance in azure : I personnally used a ubuntu server 22.04 LTS with opened SSH port 22 
2. Start the instance, the azure console should look like this:
3. Connect to the instance in ssh using the private key given at the VM creation: I used vscode server

4. install and start Docker Engine
#### Install [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
```bash
make install_docker
```

5. Kafka setup
#### Start the kafka server
```bash
make start_kafka
```

#### Create the topic: live flight position 
```bash
make create_topic
```

#### Run the producer
```bash
python src/kafka_producer.py
```
#### Run the consumer
```bash
python src/kafka_consumer.py
```



