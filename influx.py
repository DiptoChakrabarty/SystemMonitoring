from influxdb import InfluxDBClient
from datetime import datetime
from monitor.stream import get_system_data

import json

DatabaseConfig = InfluxDBClient(
            host="localhost",
            port=8086,
            username="chuck",
            password="chuck",
            database="stream",
            ssl=False,
            verify_ssl=False
)

data = get_system_data()
print("data received")
print(data)
#data = json.loads(data)
print("data loaded")
dbdata = [
            {
                "measurement": "status",
                "time": datetime.now().isoformat(),
                "fields": data,
                "tags": {
                    "monitor": "system"
                }
            }
        ]
print("writing data prepared")
DatabaseConfig.write_points(dbdata)
print("data written")
