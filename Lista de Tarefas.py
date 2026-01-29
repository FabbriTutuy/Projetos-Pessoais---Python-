# Lista de Tarefas - NÃO ESTÁ COMPLETA , PRECISA FINALIZAR

def cabecalho(msg):

    print("-"*32)
    print(f"{msg:^32}")
    print("-"*32)


def menu():

    print("-"*32)
    print("[1] Ver a lista de tarefas")
    print("[2] Adicionar uma tarefa ")
    print("[3] Excluir uma Tarefa")
    print("[4] Sair")
    print("-"*32)


cabecalho("INICIANDO PROGRAMA")

while True:

    menu()

    try:
        escolha = int(input("Oque deseja fazer: "))

    except:
        print("\033[31mTente Novamente isso não é válido!!\033[0m")

    else:
        if escolha == 4:
            print("Obrigado por usar o programa")
            break
