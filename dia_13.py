"""
    lista de dicionários

    Aí você consegue guardar:

    várias pessoas

Exemplo:

[
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 30}
]

Isso é literalmente a base de muitos sistemas e bancos de dados.
---------------------------------------------------------------------------------------

Crie:

pessoas = []

Depois:

✅ cadastrar:

nome
idade

✅ criar um dicionário para cada pessoa

✅ adicionar com:

append()

✅ mostrar todas as pessoas com for

"""

pessoas = []  #criando lista

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


cadastro = { #criei o dicionario com chave nome e valor nome
    "nome": nome,
    "idade": idade
}

pessoas.append(cadastro) # inclui na lista pessoas e cadastro (nome e idade)

for pessoa in pessoas: # para cada pessoa(variavel temporaria) na lista pessoas mostrar cadastro.
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")



    

    

