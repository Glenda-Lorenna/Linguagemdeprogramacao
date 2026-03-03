# GERENCIADOR DE ESPAÇO EM DISCO

import psutil

particoes = psutil.disk_partitions()

for particao in particoes:
    uso = psutil.disk_usage(particao.mountpoint)
    print(f"Ponto de montagem: {particao.mountpoint}")
    print(f"Espaço total: {uso.total / (1024**3):.2f} GB")
    print(f"Espaço usado: {uso.used / (1024**3):.2f} GB")
    print(f"Espaço livre: {uso.free / (1024**3):.2f} GB")
    print(f"Porcentagem usada: {uso.percent}%\n")