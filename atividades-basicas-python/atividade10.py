#ARQUIVO: SALVA E LÊ TAREFAS

def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a") as file:
        file.write(tarefa + "\n")

def listar_tarefas():
    with open("tarefas.txt", "r") as file:
        tarefas = file.readlines()
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa.strip()}")

while True:
    print("1. Adicionar uma tarefa")
    print("2. Listar tarefas")
    print("3. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        tarefa = input("Digite a tarefa a ser adicionada: ")
        adicionar_tarefa(tarefa)
    elif escolha == 2:
        listar_tarefas()
    elif escolha == 3:
        break