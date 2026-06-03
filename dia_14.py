""" 

Sistema de Cadastro de Alunos

Menu:

1 - Cadastrar aluno
2 - Listar alunos
3 - Sair
---------
Cada aluno terá:

Nome
Nota
----------
Objetivo

Quando cadastrar:

Nome: Ana
Nota: 8

Guardar em uma lista.
----------------
Depois:

Nome: Pedro
Nota: 6

Guardar também.
----------------------
Quando escolher:

2 - Listar alunos

Mostrar:

---------
Nome: Ana
Nota: 8

---------
Nome: Pedro
Nota: 6

------------------------------------------------------

>>>>>> O que é uma lista? <<<<<<<<<<

Lista é uma estrutura usada para armazenar vários valores em um único lugar.

------------------------
>>>>>> O que é um dicionário? <<<<<<<<<<

Dicionário é uma estrutura que guarda informações usando chave e valor.


Mas lembre-se: um dicionário também pode existir sozinho.
----------------------------

>>>>>> O que faz um for? <<<<<<<<<<

For percorre uma lista item por item.
---------------------------
>>>>>> O que faz um while? <<<<<<<<<<

O while executa um bloco de código enquanto uma condição for verdadeira.
--------------------------

>>>>>> Para que serve uma função? <<<<<<<<<<

Funcao serve para organizar melhor o codigo e podemos reutiliza-la quando for necessaria. 

organizar o código
evitar repetição
reutilizar tarefas

"""



alunos = [] #lista de alunos

opcoes = "0"

media = 0

def cadastrar_aluno():#funcao para cadastrar o aluno 

    
    nome = input("Digite o nome do Aluno: ") # dentro da funcao pedi nome 
    nota = int(input("Digite a nota do Aluno: "))# dentro da funcao pedi nota

    aluno = { # dicionario com os dados do aluno e nota
        "nome": nome,
        "nota": nota
    }

    alunos.append(aluno) # dentro da lista alunos inclui o nome e nota do aluno digitado 

def listar_aluno():

    if not alunos:
        print("LISTA VAZIA!")

    else:
        for aluno in alunos:
            print("---------")
            print(f"Nome: {aluno['nome']}")
            print(f"Nota: {aluno['nota']}")

def media_alunos():

    print(['nota'])
    


while opcoes != "3":

    print("-----MENU--------") # MENU PRINCIPAL
    print("1 = CADASTRAR ALUNO")
    print("2 = LISTAR ALUNO")
    print("3 = SAIR DO SISTEMA")
    print("4 = CALCULAR MEDIA ALUNOS")

    opcoes = input("Digite sua opcao: ")

    if opcoes == "1":
        cadastrar_aluno()

    elif opcoes == "2":
        listar_aluno()

    elif opcoes == "3":
        print("Sistema Finalizado!")
    
    elif opcoes == "4":
        print(media_alunos)

    else:
        print("Opcao invalida!")


