# MONITOR DE USO DE MEMÓRIA RAM COM ALERTA

import psutil
import time

limite = float(input("Digite o limite de uso de RAM em %: "))

while True:
    mem = psutil.virtual_memory()
    if mem.percent > limite:
        print(f"Alerta: Uso de RAM superior a {limite}% ({mem.percent}%)")
    
    time.sleep(2)