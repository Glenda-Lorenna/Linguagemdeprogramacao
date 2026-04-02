# MONITOR DE TRÁFEGO DE REDE

import psutil
import time

while True:
    io = psutil.net_io_counters()
    download = io.bytes_recv
    upload = io.bytes_sent

    time.sleep(1)
    novo_io = psutil.net_io_counters()
    novo_download = novo_io.bytes_recv
    novo_upload = novo_io.bytes_sent

    download_velocidade = (novo_download - download) / 1024
    upload_velocidade = (novo_upload - upload) / 1024

    print(f"Download: {download_velocidade} kB/s | Upload: {upload_velocidade} kB/s")