""" 
    Projeto:

    Sistema simples de cadastro

    Seu sistema deve:

    ✅ ter uma função
    ✅ pedir:

    nome
    idade

    ✅ dizer:

    maior de idade
    menor de idade

    ✅ perguntar se deseja continuar

    ✅ repetir com while

"""








def dados(): # criei uma função dados que pedi nome/idade ao usuario e o resultado
            #informa se a pessoa e maior ou menor de idade 

    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

    
dados() # chamo a funçaõ

continuar = input("Deseja continuar? s/n \n") # pergunto se a pessoa quer continuar e responder de novo

while continuar == "s": # se "s" sim 
    dados() # chamo a função novamente
    continuar = input("Deseja continuar? s/n \n")# apos pergunta novamente se quer continuar e responder nome/idade 
        

print("SISTEMA FINALIZADO")
     #se a resposta for não o sistema finaliza.


