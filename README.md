# SystemMonitoringRabbitMQGrafanaInflux

- This repository has code to setup a system monitoring tool
- The tools used are the follows
    * Python3.6
    * Docker
    * RabbitMQ
    * InfluxDB
    * Grafana
- The directories have the following code
    * database: setup influxdb database connection
    * monitor:  collect system metircs like cpu usage , network usage etc
    * rabbitmq: rabbitmq server and client configuration and processes setup


## Steps to Run
```bash
- Create directories grafana_data , rabbitmq_data , influxdb_data
- Provide permissions to the grafana directory
  sudo chown -R $USER grafana_data
  sudo chmod -R 777 grafana_data
- setup virtualenv using any of your preferred step
   virtualenv venv
   source venv/bin/activate
- Install packages required
   pip3 install -r requirements.txt
- Start the containers using the docker compose file
   sudo docker-compose up -d
- Add influxdb as a datasource in grafana
- Start the server and client scripts seperately
   python3 server.py
   python3 client.py
- Setup grafana dashboards
```

## Images to Get you started

- Start docker compose and server client

  ![Docker Setup](https://github.com/SystemMontoring/blob/main/images/docker.png)

- Run all scripts
   ![Scripts](https://github.com/SystemMontoring/blob/main/images/setup.png)

- RabbitMq Queue Setup which happens through code
   ![Rabbitmq Queue](https://github.com/SystemMontoring/blob/main/images/queue.png)

- RabbitMq Message Viewing
  ![MesgView](https://github.com/SystemMontoring/blob/main/images/message.png)

- Grafana DashBoard View
  ![DashBoard View](https://github.com/SystemMontoring/blob/main/images/dashboard.png)