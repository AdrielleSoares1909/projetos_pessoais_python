""" 

Sistema de múltiplos cadastros

Seu programa deve:

✅ cadastrar várias pessoas
✅ usar while
✅ guardar tudo na lista
✅ mostrar TODOS no final usando for

🧩 Fluxo mental

Pensa assim:

enquanto quiser continuar:

    pedir nome
    pedir idade

    criar cadastro

    adicionar na lista

Depois:

mostrar todas as pessoas cadastradas

"""

opcoes = "0"

pessoas = []




def cadastrar():
        
        nome = input("Digite o nome da pessoa a ser cadastrada: ")
        idade = int(input("Digite a idade da pessoa para cadastro: "))

        

        cadastro = {
            "nome": nome,
            "idade":idade
            }    

        pessoas.append(cadastro)
       
        

def listar():

               
    if not pessoas:
        print("Lista Vazia")

    else:
        for pessoa in pessoas:
            print("---------")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            



while opcoes != "3":


    print("-----menu-----")
    print("-----1 = cadastrar-----")
    print("-----2 = listar-----")
    print("-----3 = sair -----")

    opcoes =  input("Digite sua opcao: ")

    if opcoes == "1":
        cadastrar()

    elif opcoes == "2":
        listar()

    elif opcoes == "3":
        print("Sistema Finalizado")
    else:
        print("opcao invalida!")


 


        
    




    
    
















