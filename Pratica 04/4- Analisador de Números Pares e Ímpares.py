"""4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".
* Informar se o número digitado é par ou ímpar.
* Ao final, exibir a quantidade total de números pares e ímpares informados.
* Tratar entradas inválidas com mensagens de erro apropriadas.  """

numeros = []
pares = []
impares = []
total_par = 0
total_impar = 0

while True:
    entrada = input("Digite um número ou 'fim' para sair: ")

    if entrada.lower() == "fim":
        print("Encerrando o programa...")

        if numeros:
            print("Números digitados:", numeros)
            print("Pares:", pares)
            print("Ímpares:", impares)
            print("Quantidade numeros pares:", total_par)
            print("Quantidade numeros impares:", total_impar)

        else:
            print("Nenhum número foi digitado.")
        break

    try:
        numero = int(entrada)
        numeros.append(numero)

        if numero % 2 == 0:
            pares.append(numero)
            total_par += 1
        else:
            impares.append(numero)
            total_impar += 1

    except ValueError:
        print("Entrada inválida! Por favor, digite um número ou 'fim'.")