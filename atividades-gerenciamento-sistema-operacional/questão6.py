# MONITOR DE DESEMPENHO DA CPU

import psutil
import time

while True:
    cpu_total = psutil.cpu_percent()
    cpu_por_core = psutil.cpu_percent(percpu=True)

    print(f"CPU Total: {cpu_total}%")
    for i, core in enumerate(cpu_por_core):
        print(f"Núcleo {i}: {core}%")

    time.sleep(1)