"""4- Leitura e Escrita de Arquivo JSON
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
* Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo."""

import json

pessoa = {
    "nome": "Simone",
    "idade": 39,
    "cidade": "São Paulo"
}
nome_arquivo = input("Digite o nome do arquivo JSON: ")

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso em '{nome_arquivo}'.")


except Exception as erro:
    print(f"Erro ao salvar os dados: {erro}")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados_carregados = json.load(arquivo_json)
        print("Dados lidos do arquivo:")
        print(dados_carregados)

except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")

except Exception as erro:
    print(f"Erro ao ler o arquivo: {erro}")
