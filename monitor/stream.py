import shutil
import psutil

def get_system_data():
    statistics = {}

    cpu_freq = psutil.cpu_freq()
    memory = psutil.virtual_memory()
    net_speed = psutil.net_io_counters()
    _, _, free = shutil.disk_usage("/")

    statistics['physicallogicalcpucount'] = psutil.cpu_count(logical=True)

    statistics['cpufrequency'] = cpu_freq.current

    statistics['memoryavailable'] = memory.available

    statistics['memoryused'] = memory.used

    statistics['memoryfree'] = memory.free

    #statistics['internet_speed'] = net_speed

    statistics['totalmemory'] = (int(memory.total)) / (1024 * 1024 * 1024)

    statistics['cpuusage'] = psutil.cpu_percent()

    statistics["ramused"] = memory.used

    statistics["datasent"] = net_speed.bytes_sent

    statistics["datareceived"] = net_speed.bytes_recv

    statistics["freedisk"] = free


    return statistics