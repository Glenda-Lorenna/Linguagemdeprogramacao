# Cálculo do volume de um cilindro regular

raio = float(input("Digite o valor do raio da base do cilindro (cm): "))
altura = float(input("Digite o valor da altura do cilindro (cm): "))
pi = 3.14159

volume = pi * (raio ** 2) * altura
print(f"O volume do cilindro é: {volume} cm³")

