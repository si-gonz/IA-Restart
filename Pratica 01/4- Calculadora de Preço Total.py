"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra.
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
preco_total = 0

preco_total = preco_unitario * quantidade
print("Produtos - ", nome_produto, " - Preço total:", preco_total)