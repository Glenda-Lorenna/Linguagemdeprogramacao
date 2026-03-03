#LISTA DE NÚMEROS: MAIOR, MENOR E MÉDIA

N = int(input("Quantos números deseja digitar? "))
numeros = []

for i in range(N):
    valor = float(input("Digite um número: "))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / N

print("Maior número:", maior)
print("Menor número:", menor)
print("Média:", media)
