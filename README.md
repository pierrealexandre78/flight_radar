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

4. install and start Docker Engine . Verify that Docker is set up properly by ensuring that no errors are output when you run docker info in your terminal.
#### Install [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# install the docker package
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# verify that the installation is successful by installing the hello_world image
sudo docker run hello-world
```

6. Kafka Confluent setup
#### Install kafka
```bash
make install_kafka
```
#### Start the kafka server
```bash
sudo confluent local kafka start
```

#### Create the topic: live flight position 
```bash
sudo confluent local kafka topic create live_flight_positions_full_france
```

4. Run the producer locally or on another VM.

5. Run the consumer locally or on another VM.


