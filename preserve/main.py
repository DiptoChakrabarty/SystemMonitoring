import logging

from rabbitmq.RabbitMq import RabbitMqConfig,ReceiveMq

logger = logging.getLogger(__name__)

sysconfig = RabbitMqConfig(queue="entry",host="localhost",routing_key="entry")

DataBaseReceiver = ReceiveMq(config=sysconfig)

DataBaseReceiver.consume()