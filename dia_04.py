"""🔁 while — REPETIÇÃO"""
""" Crie um programa que:

1️⃣ comece em 1
2️⃣ conte até 10
3️⃣ mostre os números na tela 


Todo while precisa de 3 coisas:

1. começo
2. condição
3. mudança

Meu código:

começo → numero = 0

condição → numero < 10

mudança → numero = numero + 1


Meu código:

começo → numero = 0

condição → numero < 10

mudança → numero = numero + 1

Sem a mudança → trava infinito."""

print("----------Exercicio 01-----------")

numero = 0

while numero < 10: 
    numero += 1
    print(numero)


print("----------Exercicio 02------------")
""" Crie o sistema de senha: 

1️⃣ defina uma senha correta (ex: "1234")
2️⃣ peça senha ao usuário
3️⃣ enquanto estiver errada → pedir novamente
4️⃣ quando acertar → mostrar:

"""


senha = 1234

senha_digitada = int(input("Digite sua senha: "))

while senha != senha_digitada:
        
        senha_digitada = int(input("Digite sua senha novamente: "))

print("Senha ok.")

    
    


