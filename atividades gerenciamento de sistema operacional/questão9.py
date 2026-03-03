# LISTAGEM DE DISPOSITIVOS DE ENTRADA E SAÍDA

import psutil

# Listar dispositivos de armazenamento (HDs/SSDs/pendrives)
particoes = psutil.disk_partitions()
print("Partições de armazenamento:")
for particao in particoes:
    print(particao.device)

# Mostrar informações detalhadas de um dispositivo/partição escolhido pelo usuário
escolha = input("Escolha um dispositivo/partição para informações detalhadas: ")
for particao in particoes:
    if particao.device == escolha:
        uso = psutil.disk_usage(particao.mountpoint)
        print(f"Ponto de montagem: {particao.mountpoint}")
        print(f"Espaço total: {uso.total / (1024**3):.2f} GB")
        print(f"Espaço usado: {uso.used / (1024**3):.2f} GB")
        print(f"Espaço livre: {uso.free / (1024**3):.2f} GB")
        print(f"Porcentagem usada: {uso.percent}%")
        break