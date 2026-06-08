""" 
O que o sistema precisa fazer?

Sistema de alunos

1 - Cadastrar
2 - Listar
3 - Buscar aluno pelo nome
4 - Sair
--------------------------
Opção 1 - Cadastrar

Perguntas:

Qual o nome do aluno?
Qual a nota do aluno?

Depois:

Criar um dicionário
Adicionar na lista alunos

-----------------------------------
Opção 2 - Listar

Pergunta:

A lista está vazia?

Se sim:

Lista vazia

Se não:

Percorrer a lista com for
Mostrar nome e nota

------------------------------------

3 - Buscar aluno pelo nome

-------------------------------------

4 - Sair

"""



alunos = []

opcao = "0"

def cadastrar_aluno():

    nome = input("Digite o nome do aluno: ")
    nota = int(input("Digite a nota do aluno: "))

    aluno = {
        "nome": nome,
        "nota": nota
    }

    alunos.append(aluno)


def listar_aluno():

    if not alunos:
        print("LISTAR VAZIA")
    
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Nota: {aluno['nota']}")

def buscar_aluno():

    localizar_aluno = input("Qual nome deseja procurar na Lista de Cadastro??? ")

    encontrei_aluno = False

    for aluno in alunos:

        if aluno["nome"] == localizar_aluno:
            encontrei_aluno = True
            
            print(f"Nome: {aluno['nome']}")
            print(f"Nota: {aluno['nota']}")

    if not encontrei_aluno:
        print("NÃO ENCONTREI ESSE ALUNO! ")
    
            
while opcao != "4":

    

    print("----- MENU ALUNOS ------")
    print("1 - CADASTRAR ALUNO ")
    print("2 - LISTAR ALUNO ")
    print("3 - BUSCAR ALUNO - > NOME < ")
    print("4 - SAIR DO SISTEMA!!! ")

    opcao = input("Digite sua opcao: ")

    
    if opcao == "1":

        cadastrar_aluno()

    elif opcao == "2":

        listar_aluno()

    elif opcao == "3":

        buscar_aluno()

    else:
        print("SAIR DO SISTEMA!!!")