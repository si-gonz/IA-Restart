"""3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".
* Verificar se a senha possui pelo menos 8 caracteres.
* Verificar se contém pelo menos um número.
* Informar se a senha é fraca ou forte.
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".
"""

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()


    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    try:

        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres!")

        if not any(caractere.isdigit() for caractere in senha):
            raise ValueError("A senha deve conter pelo menos um número.")

        print("Senha cadastrada com sucesso!")
        break

    except ValueError as erro:
        print("Senha não atende os requisitos")