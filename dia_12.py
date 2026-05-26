""" dicionários (dict)

Aí você começa a guardar:

nome + idade

produto + preço

-------------------------

Crie um dicionário:

pessoa = {}

Depois:

✅ pedir:

nome
idade

✅ guardar no dicionário

"""

#pega os dados primeiro

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

#depois monta o dicionário

pessoa = {
    "nome": nome, # chave = nome / valor = nome
    "idade": idade # chave = idade / valor = idade 
    }


print(f"Nome: {pessoa["nome"]}")
print(f"Idade: {pessoa["idade"]}")