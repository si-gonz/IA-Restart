"""3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.
* Solicitar o percentual de desconto desejado.
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def entrada_val():
    valor = float(input(" Digite o valor do produto: "))
    return valor;

def entrada_desc():
    desconto = float(input(" Digite a porcentagem do desconto: "))
    return desconto;

def calculo (valor, desconto):
    return valor * (desconto/100);

valor = entrada_val()
porcentagem = entrada_desc()
desconto = calculo(valor, porcentagem)

print(f" O valor do desconto é: R${desconto:.2f}")



