# PAINEL INTEGRADO DE MONITORAMENTO

import psutil
import os
import time

while True:
    # Uso de RAM
    mem = psutil.virtual_memory()
    total_ram = mem.total / (1024**3)
    uso_ram = mem.used / (1024**3)

    # Uso de CPU
    uso_cpu = psutil.cpu_percent()

    # Espaço livre na partição principal
    disco = psutil.disk_usage('/')
    espaco_livre = disco.free / (1024**3)

    # Taxa de download/upload aproximada
    io = psutil.net_io_counters()
    download = io.bytes_recv
    upload = io.bytes_sent
    time.sleep(1)
    novo_io = psutil.net_io_counters()
    download_velocidade = (novo_io.bytes_recv - download) / 1024
    upload_velocidade = (novo_io.bytes_sent - upload) / 1024

    # Limpar tela
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Mostrar informações no console
    print(f"Uso de RAM: {uso_ram:.2f}/{total_ram:.2f} GB")
    print(f"Uso de CPU: {uso_cpu}%")
    print(f"Espaço livre na partição principal: {espaco_livre:.2f} GB")
    print(f"Download: {download_velocidade:.2f} kB/s | Upload: {upload_velocidade:.2f} kB/s")

    time.sleep(2)