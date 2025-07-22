"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

nome_produto = " Camiseta"
preco_original = 50.00
desc = 0.20
valor_desc = 0
valor_final = 0

valor_desc = preco_original * desc
valor_final = preco_original - valor_desc

print(f"Produto: {nome_produto}")
print(f"Preço original: R${preco_original:.2f}")
print(f"Desconto: {desc * 100:.0f}%")
print(f"Valor do desconto: R${valor_desc:.2f}")
print(f"Preço final com desconto: R${valor_final:.2f}")