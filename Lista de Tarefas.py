from rich import print

# =-=-= VARIAVEIS =-=-=

arquivo = "tarefas.txt"
funcoes = ["Ver lista de tarefas","Adicionar uma tarefa","Excluir uma tarefa","Sair"]

# =-=-= FUNÇÕES =-=-=

def cabecalho(msg):

    print("-"*32)
    print(f"{msg:^32}")
    print("-"*32)


def menu():

    cabecalho("MENU PRINCIPAL")

def ArquivoExiste(nome_do_arquivo):

    try:
        a = open(nome_do_arquivo,"rt")
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True
    
def CriarArquivo(nome_do_arquivo):
    
    try:
        a = open(nome_do_arquivo,"wt+")
        a.close()

    except:
        print("[bold red]Erro na criação do arquivo! Tente Novamente.[/]")

    else:
        print("[bold green]Criação do Arquivo foi um sucesso[/]")

# =-=-= PROGRAMA =-=-=

if not ArquivoExiste(arquivo):
    CriarArquivo(arquivo)

cabecalho("INICIANDO PROGRAMA")

while True:

    try:
        escolha = int(input("Oque deseja fazer: "))

    except:
        print("\033[31mTente Novamente isso não é válido!!\033[0m")

    else:
        if escolha == 4:
            print("Obrigado por usar o programa")
            break
