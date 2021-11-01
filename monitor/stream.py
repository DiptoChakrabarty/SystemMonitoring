import shutil
import psutil

def get_system_data():
    statistics = {}

    cpu_freq = psutil.cpu_freq()
    memory = psutil.virtual_memory()
    net_speed = psutil.net_io_counters()
    _, _, free = shutil.disk_usage("/")

    statistics['physical_and_logical_cpu_count'] = psutil.cpu_count(logical=True)

    statistics['cpu_frequency'] = cpu_freq

    statistics['virtual_memory'] = memory

    statistics['internet_speed'] = net_speed

    statistics['total_memory'] = (int(memory.total)) / (1024 * 1024 * 1024)

    statistics['cpu_usage'] = psutil.cpu_percent()

    statistics["ram_used"] = memory.used

    statistics["data_sent"] = net_speed.bytes_sent

    statistics["data_received"] = net_speed.bytes_recv

    statistics["free_disk"] = free


    return statistics





