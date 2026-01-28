import secrets
import string
import random

DEFAULT_SYMBOLS = '!@#$%^&*()-_=+[]{};:,.<>/?'


def gerar_senha(tamanho=12, incluir_numeros=True, simbolos=DEFAULT_SYMBOLS, palavra=None):
    """Gera uma senha com as opções solicitadas.

    Args:
        tamanho (int): comprimento total desejado da senha.
        incluir_numeros (bool): se deve incluir dígitos.
        simbolos (str|None): string com símbolos a serem usados ('' ou None para nenhum).
        palavra (str|None): palavra que deve estar incluída na senha (opcional).

    Returns:
        str: senha gerada.
    """
    letras = string.ascii_letters
    digitos = string.digits if incluir_numeros else ''
    simbolos = simbolos or ''

    pool = letras + digitos + simbolos
    if not pool and not palavra:
        raise ValueError("Nenhum caractere disponível para gerar a senha.")

    senha_chars = []

    # Garantir variedade quando possível
    if letras:
        senha_chars.append(secrets.choice(string.ascii_lowercase))
        senha_chars.append(secrets.choice(string.ascii_uppercase))
    if digitos:
        senha_chars.append(secrets.choice(digitos))
    if simbolos:
        senha_chars.append(secrets.choice(simbolos))

    # Começar com a palavra fixa se houver
    if palavra:
        senha_chars = list(palavra) + senha_chars

    # Preencher o restante
    restante = max(0, tamanho - len(senha_chars))
    for _ in range(restante):
        senha_chars.append(secrets.choice(pool))

    # Embaralhar de forma segura
    random.SystemRandom().shuffle(senha_chars)
    return ''.join(senha_chars[:tamanho])


def pergunta_simples(pergunta, opcoes_validas):
    """Lê do usuário até obter uma resposta válida (opções em minúsculo)."""
    while True:
        resp = input(pergunta).strip().lower()
        if resp in opcoes_validas:
            return resp
        print("Resposta inválida. Digite uma opção válida.")


def main():
    print("--- Gerador de Senhas ---")

    # Tamanho
    while True:
        try:
            tamanho = int(input("Tamanho da senha (ex: 12): ").strip())
            if tamanho <= 0:
                print("Informe um número inteiro maior que 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o tamanho.")

    # Incluir números
    incluir_numeros = pergunta_simples("Incluir números? (s/n): ", {"s", "n"}) == "s"

    # Incluir símbolos e quais
    usar_simbolos = pergunta_simples("Incluir símbolos? (s/n): ", {"s", "n"}) == "s"
    simbolos = ''
    if usar_simbolos:
        simbolos_input = input(f"Quais símbolos deseja usar? (deixe vazio para usar o padrão: {DEFAULT_SYMBOLS}): ").strip()
        simbolos = simbolos_input if simbolos_input != '' else DEFAULT_SYMBOLS

    # Palavra específica
    tem_palavra = pergunta_simples("Deseja incluir uma palavra específica dentro da senha? (s/n): ", {"s", "n"}) == "s"
    palavra = None
    if tem_palavra:
        while True:
            palavra = input("Digite a palavra que deve ficar dentro da senha: ").strip()
            if palavra == '':
                print("Palavra não pode ser vazia.")
                continue
            if len(palavra) > tamanho:
                print(f"A palavra tem {len(palavra)} caracteres, maior que o tamanho informado ({tamanho}).")
                ajustar = pergunta_simples("Deseja aumentar o tamanho para acomodar a palavra? (s/n): ", {"s", "n"})
                if ajustar == "s":
                    tamanho = len(palavra)
                    print(f"Tamanho ajustado para {tamanho}.")
                    break
                else:
                    print("Digite outra palavra ou aumente o tamanho.")
                    continue
            break

    # Gerar e mostrar
    try:
        senha = gerar_senha(tamanho=tamanho, incluir_numeros=incluir_numeros, simbolos=simbolos, palavra=palavra)
        print(f"Senha gerada: {senha}")
    except ValueError as e:
        print("Erro ao gerar senha:", e)


if __name__ == '__main__':
    main()