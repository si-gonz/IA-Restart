"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_reais = 100.00
valor_reais = 100.00
tx_dolar = 5.20
tx_euro = 6.15

conv_dolar = valor_reais / tx_dolar
conv_euro = valor_reais / tx_euro

print(f"O valor de R${valor_reais:.2f} convertido em dólar é: ${conv_dolar:.2f}")
print(f"O valor de R${valor_reais:.2f} convertido em euro é: €{conv_euro:.2f}")