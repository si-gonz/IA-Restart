"""Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais)."""

idade = int(input("Digite sua idade: "))

if (idade >= 0) and (idade <= 12):
    print("O usuário é uma criança.")
elif (idade >= 13) and (idade <= 17):
    print("O usuário é um adolescente.")
elif (idade >= 18) and (idade <= 59):
    print("O usuário é um adulto.")
elif (idade >= 60):
    print("O usuário é um idoso.")
else:
    print("Idade inválida.")