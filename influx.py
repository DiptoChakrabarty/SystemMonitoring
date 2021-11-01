from influxdb import InfluxDBClient
from datetime import datetime

client = InfluxDBClient('localhost',8086,'admin','toor','stream')
client.get_list_database()