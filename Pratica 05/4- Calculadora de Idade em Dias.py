"""4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.
* Considere o ano atual automaticamente.
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).
* Exiba o resultado final."""
from datetime import datetime

def entrada():
    ano_atual = datetime.today().year

    while True:
        try:
            ano_nascimento = int(input("Digite o seu ano de nascimento: "))
            if ano_nascimento <= 0 or ano_nascimento > ano_atual:
                print("Digite um ano de nascimento válido.")
            else:
                return ano_nascimento
        except ValueError:
            print("Digite apenas números para o ano.")

def calculo(ano_nascimento):
    ano_atual = datetime.today().year
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    return idade_em_dias


ano_nascimento = entrada()
dias = calculo(ano_nascimento)
print(f"\nVocê tem aproximadamente {dias} dias de vida.")
