"""2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".
* Somente notas entre 0 e 10 devem ser aceitas.
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.
* Trate entradas inválidas com mensagens de erro.
"""

notas = []
soma = 0
media = 0

while True:
    entrada = input("Digite a nota do aluno ou 'fim' para sair: ")

    if entrada.lower() == "fim":
        print("Encerrando o programa...")
        if notas:
            print("Notas digitadas:", notas)
            print("Média:", media)
        else:
            print("Nenhuma nota foi digitada.")
        break

    try:
        nota = float(entrada)
        notas.append(nota)
        soma += nota
        media = soma / len(notas)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número ou 'fim'.")