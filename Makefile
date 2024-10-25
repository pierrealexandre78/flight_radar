all: build_env pip

pip:
	sudo apt install python3-pip
	pip install -r requirements.txt

install_env:
# install pyenv
	curl https://pyenv.run | bash;
	sudo apt  install direnv;
# Pyenv
	export PYENV_ROOT="$HOME/.pyenv"
	command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"
	sudo apt install python3.12-venv

create_env:
# create new_env
	pyenv virtualenv flight_radar_env
	pyenv activate flight_radar_env
	pyenv local flight_radar_env

install_docker:
#Add Docker's official GPG key:
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

start_kafka:
	sudo docker-compose up -d

check_kafka:
# let’s use the nc command to verify that both the servers are listening on the respective ports
	nc -zv localhost 22181
	nc -zv localhost 29092
# verify that the Kafka server is up:
	sudo docker-compose logs kafka | grep -i started

create_topic:
# create kafka topic named live_flight_positions_full_france
	sudo docker-compose exec kafka kafka-topics --create --topic live_flight_positions_full_france --bootstrap-server localhost:29092 --partitions 1 --replication-factor 1

stop_kafka:
	sudo docker-compose down




