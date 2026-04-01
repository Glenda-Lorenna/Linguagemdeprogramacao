# Área de um Cilindro Regular

raio = float(input("Digite o valor do raio da base do cilindro (cm): "))
altura = float(input("Digite o valor da altura do cilindro (cm): "))
pi = 3.14159

area_lateral = 2 * pi * raio * altura
area_base = pi * (raio ** 2)
area_total = area_lateral + 2 * area_base
print(f"A área total do cilindro é: {area_total} cm²")
