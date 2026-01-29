# Lista de Tarefas - NÃO ESTÁ COMPLETA , PRECISA FINALIZAR
import pandas as pd

listas_de_afazeres = 0

while True:
    tarefa = input("Digite uma tarefa para adicionar à lista (ou 'sair' para encerrar): ")

    if tarefa.lower() == 'sair':
        print("Encerrando o programa de lista de tarefas.")
        break   

    elif tarefa.strip() == "":
        print("Você não digitou nenhuma tarefa. Tente novamente.")
        continue

    elif tarefa in tarefas:
        print("Essa tarefa já está na lista.")
        continue

    else:
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista.")
        tarefa = datetime.now()
        print(f"Essa tarefa foi adicionado :{tarefa}")

print("\nSua lista de tarefas:")
for idx, tarefa in enumerate(tarefas, start=1):
    print(f"{idx}. {tarefa}")