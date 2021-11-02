import time
import logging

from rabbitmq.RabbitMq import RabbitMqConfig,ServerMq
from stream import get_system_data

logger = logging.getLogger(__name__)

sysconfig = RabbitMqConfig(queue="entry",host="localhost",routing_key="entry")

SystemServer = ServerMq(config=sysconfig)

while True:
    try:
        data = get_system_data()
        logger.info("Data Received")
    except Exception as e:
        logger.error(f"Data not received error : {e}")
        break
    
    try:
        SystemServer.publish(data)
        time.sleep(2000)
        logger.info("Data Transmitted , sleeping for two seconds")
    except Exception as e:
        logger.error(f"Unable to transmit data : {e}")
        

