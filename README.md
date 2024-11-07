# Apache Kafka - Live Flight Data streaming

Technology used: *Azure (VM, Blob Storage, Azure Functions, Azure Devops, Azure Data Lake Analytics, Azure Synapse), Kafka, Spark, python*

## Abstract

The goal of the project was to get to know how Apache Kafka streams works. For training purposes, I used an Azure free D2S machine and simulated the stream of the data to avoid memory problems on the Azure instance. Each event in the simulated streaming was created as a sample JSON file from an existing dataset. The streamed data was uploaded to an Azure Blob Storage and analyzed by a Data Factory, which created a table schema in the Azure Data Lake Analytics. That allowed me to perform queries in Azure Synapse Analytics.

## Data Flow

![Project Architecture](/images/project_architecture.png)

## Installation

### Pre-requisite:
* active Azure account subscription

### Kafka server setup
Setup Kafka server on Azure VM:

1. Create a VM instance in azure : I personally used a ubuntu server 24.04 LTS
2. Start the instance, the azure console should look like this:   ![](/images/az_vm.JPG)
3. Kafka port: create an inbound security rule for port 9092 ![](/images/kafka_port.JPG)
4. Connect to the instance in ssh using the private key given at the VM creation
5. install and start [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) Engine on the instance
```bash
make install_docker
```

![](/images/vscode_docker_install.JPG)

6. Kafka setup
#### Start the kafka server
```bash
make start_kafka
```
#### Create the topic: live flight position 
```bash
make create_topic
```

7. Create the storage account and blob storage in azure console
![](/images/blob_storage.JPG)
![](/images/create_flight_data_az_container.JPG)
![](/images/az_storage_connection_string.JPG)

#### Run the producer
```bash
python src/kafka_producer.py
```
#### Run the consumer
```bash
python src/kafka_consumer.py
```

### Azure Functions
The Goal is to create an azure function that will copy the live data (streamed by kafka into blob storage) every 10 mn into azure data lake gen2
1. create a new azure function app in azure portal
2. install azure function extension in your vscode, don't forget to connect to your azure account
3. install azure cli in your terminal and connect. this installation is needed to add azure application environement variable to connect to blob storage and data lake storage
```bash
make install_azure_cli
```
verify that the installation worked and connnects to your azure account
```bash
az login
```
4. Use the azure cli to add your connection string
add your blob storage and data lake connection strings as environement variable for your azure function app
```bash
az functionapp config appsettings set --name <FunctionAppName> --resource-group <ResourceGroupName> --settings "BLOB_CONNECTION_STRING=your_blob_connection_string"
```
Replace <FunctionAppName> with the name of your Function App, <ResourceGroupName> with the name of your resource group, and your_blob_connection_string with your actual connection string.


