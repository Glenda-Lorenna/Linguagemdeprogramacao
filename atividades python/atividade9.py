def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("Escolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    escolha = int(input("Digite o número da operação desejada: "))

    if escolha == 5:
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == 1:
        print("Resultado: ", somar(a, b))
    elif escolha == 2:
        print("Resultado: ", subtrair(a, b))
    elif escolha == 3:
        print("Resultado: ", multiplicar(a, b))
    elif escolha == 4:
        print("Resultado: ", dividir(a, b))