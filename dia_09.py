""" Sistema de lista de compras

Crie:

compras = []

Depois:

✅ peça 3 produtos
✅ adicione na lista
✅ mostre:

LISTA DE COMPRAS

✅ use for para mostrar os produtos um por um

⭐ Desafio bônus (nível júnior)

Mostrar assim:

- arroz
- feijão
- leite

"""






produto1 = input("Digite o primeiro produto da lista: ")
produto2 = input("Digite o segundo produto da lista: ")
produto3 = input("Digite o terceiro produto da lista: ")

compras = [produto1, produto2, produto3] # lista de compras

print("----Lista de Compras------")

for compra in compras: # para cada nome dentro da lista de compras 
    print(f"- {compra}")