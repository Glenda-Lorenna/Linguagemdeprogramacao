# HISTÓRICO DE USO DA CPU

import psutil
import datetime
import time

with open("cpu_log.txt", "a") as arquivo:
    while True:
        uso_cpu = psutil.cpu_percent(interval=1)
        data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        arquivo.write(f"{data_hora} - CPU: {uso_cpu}%\n")
        
        time.sleep(4)  # 1 segundo já foi usado no interval