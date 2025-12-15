# IMPORTS 

import time

# FUNÇÕES E VARIÁVEIS

def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de a e b."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de a por b, se b não for zero."""
    if b == 0:
        return "Não é possível efetuar essa divisão"
    else:
        return a / b

def potenciacao(a, b):
    """Retorna a potenciação de a elevado a b."""
    return a ** b

def obter_numero(mensagem):
    """Obtém um número do usuário com validação."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def menu():
    """Exibe o menu da calculadora."""
    print("\nCalculadora")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Potenciação")
    print("[6] Sair do programa")

# PARTE FUNCIONAL DA CALCULADORA

total_de_contas = 0
contas_de_subtracao = 0
contas_de_adicao = 0
contas_de_multiplicacao = 0
contas_de_divisao = 0
contas_de_potenciacao = 0

while True:
    time.sleep(1.2)
    menu()
    try:
        opcao = int(input("Qual função você deseja acessar: "))
    except ValueError:
        print("Isso não é um número")
        continue

    if opcao == 6:
        break

    if opcao in [1, 2, 3, 4, 5]:
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        if opcao == 1:
            resultado = soma(num1, num2)
            print(f"A soma de {num1} + {num2} é {resultado}")
            contas_de_adicao += 1

        elif opcao == 2:
            resultado = subtracao(num1, num2)
            print(f"A subtração de {num1} - {num2} é {resultado}")
            contas_de_subtracao += 1

        elif opcao == 3:
            resultado = multiplicacao(num1, num2)
            print(f"A multiplicação de {num1} x {num2} é {resultado}")
            contas_de_multiplicacao += 1

        elif opcao == 4:
            resultado = divisao(num1, num2)
            print(f"A divisão de {num1} / {num2} é {resultado}")
            contas_de_divisao += 1

        elif opcao == 5:
            resultado = potenciacao(num1, num2)
            print(f"A potenciação de {num1} ^ {num2} é {resultado}")
            contas_de_potenciacao += 1

        total_de_contas += 1

    else:
        print("ERROR... Essa operação não existe. Tente novamente!")

# Exibição do resumo
print(f"""Você fez um total de {total_de_contas} contas até agora.
=-=-=-=-=-=-=-=-=SENDO ELAS: =-=-=-=-=-=-=-=-=
Um total de {contas_de_adicao} de adição
Um total de {contas_de_subtracao} de subtração
Um total de {contas_de_multiplicacao} de multiplicação
Um total de {contas_de_divisao} de divisão
Um total de {contas_de_potenciacao} de potenciação

OBRIGADO VOLTE SEMPRE :) """)
