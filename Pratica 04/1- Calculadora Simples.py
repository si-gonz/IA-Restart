"""1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.
* Peça a operação desejada (+, -, *, /).
* Realize a operação escolhida e exiba o resultado.
* Trate divisões por zero e operações inválidas com mensagens apropriadas.

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso."""


while True:
    try:
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        operador = input("Digite o operador (+, -, *, /) ou 'sair' para encerrar: ")

        while True:

            if operador == "sair":
                print("Encerrando a calculadora...")
                exit()
            elif operador == "+":
                print("Resultado:", n1 + n2)
                break
            elif operador == "-":
                print("Resultado:", n1 - n2)
                break
            elif operador == "*":
                print("Resultado:", n1 * n2)
                break
            elif operador == "/":
                if n2 != 0:
                    print("Resultado:", n1 / n2)
                else:
                    print("Erro: divisão por zero!")
                break
            else:
                print("Operador inválido. Tente novamente.")

    except ValueError:
        print("Erro: por favor, digite apenas números válidos.")
