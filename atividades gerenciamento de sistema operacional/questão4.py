# ALERTA DE POUCO ESPAÇO EM DISCO

import psutil

limite = float(input("Digite o limite de espaço livre em %: "))

particoes = psutil.disk_partitions()

for particao in particoes:
    uso = psutil.disk_usage(particao.mountpoint)
    if uso.percent < limite:
        print(f"Alerta: Espaço livre inferior a {limite}% em {particao.mountpoint} ({uso.percent}%)")