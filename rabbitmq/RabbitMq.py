
from datetime import datetime
from typing import Dict
import pika
import json
from pika.spec import Exchange
from database.config import DatabaseConfig

class RabbitMqConfig:
    def __init__(self,queue:str ="sys" ,host:str ="localhost",routing_key:str ="sys") -> None:
        self.queue = queue
        self.host = host
        self.routing_key = routing_key

class ServerMq:
    def __init__(self,config: RabbitMqConfig) -> None:
        self.config = config
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.config.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)

    def publish(self,objectbody):
        self.channel.basic_publish(exchange='',
            routing_key = self.config.routing_key,
            body = json.dumps(objectbody))
        print(f"Message Sent to RabbitMq with routing key {self.config.routing_key}")
        #self.connection.close()
        #print("Connection Closed")
    
    def __del__(self):
        self.connection.close()

class ReceiveMq:
    def __init__(self,config: RabbitMqConfig) -> None:
        self.config = config
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host = self.config.host
        ))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)
    
    def consume(self):
        self.channel.basic_consume(queue=self.config.routing_key,
        on_message_callback=self.callback,
        auto_ack = True)
        print("Waiting for messages\n")
        self.channel.start_consuming()

    @staticmethod
    def callback(ch,method,properties,body):
        objectbody = json.loads(body)
        dbdata = [
            {
                "measurement": "status",
                "time": datetime.now(datetime.timezone.utc),
                "fields": objectbody,
                "tags": {
                    "monitor": "system"
                }
            }
        ]
        print(datetime.now(datetime.timezone.utc))
        DatabaseConfig.write_points(dbdata)
        print("Data Written to InfluxDB")