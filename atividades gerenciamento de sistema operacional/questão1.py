# MONITOR SIMPLES DE MEMÓRIA RAM

import psutil
import time

while True:
    mem = psutil.virtual_memory()
    total = mem.total
    usado = mem.used
    livre = mem.available

    print(f"Total de memória RAM: {total / (1024**3):.2f} GB")
    print(f"Memória em uso: {usado / (1024**3):.2f} GB")
    print(f"Memória livre: {livre / (1024**3):.2f} GB ({mem.percent}%)")

    time.sleep(2)