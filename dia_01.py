
"""
    Sistema pedi para o usuario digitar o nome, guarda na variavel nome.
    Pedi para o usuario digitar idade, guarda na variavel idade.
    Cria nova variavel para calcular a idade futura do usuario, somando a sua idade digitada mais 10.
    Printa na tela a mensagem personalizada com Bom dia, o nome do usuario, confirma a idade atual e logo depois soma a idade atual mais 10, finaliza
    informando quantos anos o usuario tera daqui 10 anos.
"""

nome = input("Digite o seu nome: ")


idade = int(input("Digite sua idade: "))

idade_futura = idade + 10


print(f"Bom dia: {nome}, sua idade é: {idade} anos, e daqui 10 anos sera: {idade_futura}")

