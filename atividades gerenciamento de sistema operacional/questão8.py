# INFORMAÇÕES DETALHADAS DO PROCESSADOR

import psutil
import platform
import subprocess

print("===== INFORMAÇÕES DO PROCESSADOR =====\n")

# Nome / Modelo da CPU
print(f"Modelo da CPU: {platform.processor()}")

# Núcleos
print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos lógicos: {psutil.cpu_count(logical=True)}")

# Frequência
freq = psutil.cpu_freq()

if freq:
    print(f"Frequência atual: {freq.current:.2f} MHz")
    print(f"Frequência máxima: {freq.max:.2f} MHz")
else:
    print("Informação de frequência não disponível.")

# Tentativa de obter número de série (Windows)
print("\nNúmero de série da CPU:")

try:
    comando = "wmic cpu get ProcessorId"
    resultado = subprocess.check_output(comando, shell=True).decode()
    linhas = resultado.strip().split("\n")

    if len(linhas) > 1 and linhas[1].strip() != "":
        print(linhas[1].strip())
    else:
        print("Número de série não disponível neste sistema.")
        
except Exception:
    print("Não foi possível obter o número de série neste sistema operacional.")