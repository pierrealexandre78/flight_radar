# Flight Radar Data

Flight Radar real-time data ingestion with Apache Kafka and Spark

### Installation

#### Pre-requisites:
* VM in azure with docker installed

Luanch Kafka servers
Using JVM Based Apache Kafka Docker Image
Get the Docker image:
```bash```
```docker pull apache/kafka:3.8.0
```

Start the Kafka Docker container:
```bash```
```docker run -p 9092:9092 apache/kafka:3.8.0
```

#### Kafka setup:

This guide runs Kafka in Docker via the Confluent CLI.

First, install and start Docker Desktop or Docker Engine if you don't already have it. Verify that Docker is set up properly by ensuring that no errors are output when you run docker info in your terminal.