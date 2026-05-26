"""

Crie um programa que:

✅ tenha lista vazia
✅ peça produto
✅ adicione na lista
✅ pergunte:

Deseja adicionar outro produto? s/n

✅ use while
✅ no final mostre todos os produtos com for

"""

lista_compras = []


produto = input("Digite o produto: ")

lista_compras.append(produto)


continuar = input("Deseja adicionar mais itens? s/n \n")

while continuar == "s":

    produto = input("Digite o produto: ")

    lista_compras.append(produto)

    continuar = input("Deseja adicionar mais itens? s/n \n")

    
for produto in lista_compras:
    
    print(f"- {produto}")
