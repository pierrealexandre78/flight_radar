all: build_env pip


create_env:
	pyenv virualenv 3.12.1 flight_radar_env
	pyenv activate flight_radar_env
	pyenv local flight_radar_env

pip:
	pip install -r requirements.txt

install_kafka:
	sudo apt install curl gnupg
    sudo mkdir -p /etc/apt/keyrings
    curl https://packages.confluent.io/confluent-cli/deb/archive.key | sudo gpg --dearmor -o /etc/apt/keyrings/confluent-cli.gpg
    sudo chmod go+r /etc/apt/keyrings/confluent-cli.gpg
	echo "deb [signed-by=/etc/apt/keyrings/confluent-cli.gpg] https://packages.confluent.io/confluent-cli/deb stable main" | sudo tee /etc/apt/sources.list.d/confluent-cli.list >/dev/null
	sudo apt update
	sudo apt install confluent-cli=3.48.0

start_kafka:
	confluent local kafka start
	confluent local kafka topic create live_flight_positions_full_france

stop_kafka:
	confluent local kafka stop


