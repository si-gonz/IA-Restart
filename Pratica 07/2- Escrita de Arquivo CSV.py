"""2- Escrita de Arquivo CSV
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""

import csv

dados_pessoas = [
    ['Simone', 40, 'São Paulo'],
    ['Cleiton', 42, 'Santo André'],
    ['Rubi', 12, 'São Paulo']
]

nome_arquivo = input("Digite o nome do arquivo CSV: ")

try:
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        arquivo = csv.writer(arquivo_csv)

        arquivo.writerow(['Nome', 'Idade', 'Cidade'])

        for pessoa in dados_pessoas:
            arquivo.writerow(pessoa)


    print(f"Dados gravados com sucesso!!'{nome_arquivo}'.")

except Exception as erro:
    print(f"Erro ao gravar o arquivo: {erro}")