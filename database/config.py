from influxdb import InfluxDBClient

DatabaseConfig = InfluxDBClient(
            host="localhost",
            port=8086,
            username="chuck",
            password="chuck",
            database="stream",
            ssl=False,
            verify_ssl=False
)