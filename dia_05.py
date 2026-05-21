""" Projeto: Cadastro simples

Seu programa deve:

1️⃣ pedir:

nome
idade

2️⃣ verificar:

se é maior de idade
ou menor de idade

3️⃣ mostrar mensagem personalizada

Exemplo:

Olá Maria
Você é maior de idade.

Adicionar:

✅ perguntar se a pessoa quer continuar
✅ usar while """


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))



if idade >= 18:
    print(f"Olá {nome}, Você é maior de Idade! ")
else:
    print(f"Olá {nome}, Você é menor de idade! ")

continuar = input("Deseja continuar ? s/n \n") 

while continuar == "s":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print(f"Olá {nome}, Você é maior de Idade! ")
    else:
        print(f"Olá {nome}, Você é menor de idade! ")

    continuar = input("Deseja continuar ? s/n \n") 







