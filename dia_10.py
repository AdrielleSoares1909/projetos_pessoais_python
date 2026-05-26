""" Crie:

compras = []

Depois:

✅ use append() para adicionar produtos
✅ mostre a lista com for

🧩 Dica mental

.append() significa:

adicionar dentro da lista

Exemplo mental:

compras.append(produto)

👉 “coloque produto dentro da lista”.

"""


compras = []

produto = input("Digite o produto: ")


compras.append(produto) #append adiciona o produto digitado dentro da lista.

for produto in compras: # para cada nome(produto) dentro da lista de compras adicionar o produto digitado.
    print(produto)

