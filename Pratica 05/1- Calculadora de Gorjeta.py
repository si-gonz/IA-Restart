"""1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais."""


def entrada():
    valor_conta = float(input("Digite o valor da conta: "))
    return valor_conta

def calculo(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta)

valor = entrada()
porcentagem = 0.15
gorjeta = calculo(valor, porcentagem)

print(f"O valor da gorjeta é: R${gorjeta:.2f}")
