import time 

moeda_real = float(input("Qual o Valor em real você tem: R$  "))

print(moeda_real)

def dolar(moeda_real):

    #VALOR DESATUALIZADO

    moeda_dolar = moeda_real / 5.52
    return f"Você Tem ${moeda_dolar:.2f} em Dólares"

def euro(moeda_real):
    
    #VALOR DESATUALIZADO

    moeda_euro = moeda_real / 6.47
    return f"Você tem €{moeda_euro:.2f} em Euro"

def menu():
    print("=-"*5,"Conversor de Moeda ","=-"*5)
    print("[1] Converter em Dólar")
    print("[2] Converter em Euro ")
    print("[3] Sair")

while True:
    print("Carregando...")
    time.sleep(0.7)
    menu()
    escolha = int(input("Qual moeda deseja converter: "))

    if escolha == 1:
        print(dolar(moeda_real))

    elif escolha == 2:
        print(euro(moeda_real))

    elif escolha == 3:
        print("Obrigado por usar o programa... Volte sempre!")
        break

    else:
        print("Isso não é um dos valores possíveis tente novamente!")

