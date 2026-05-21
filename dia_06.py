""" 
FUNÇÕES (def) 

função = mini máquina

Você cria uma vez…
e usa quando quiser.

---------------------------------------

Missão 1

Crie uma função chamada:

saudacao()

Olá, seja bem-vindo!

"""

print( " -----------Exercicio 01-------------")

def saudacao():
   
   print("Olá, Bom Dia!") 

saudacao()
    

print( " -----------Exercicio 02-------------")

""" Função de soma

✅ pedir dois números
✅ somar
✅ mostrar resultado

""" 

def somar():

    numero1 = int(input("Digite o primeiro numero: "))

    numero2 = int(input("Digite o segundo numero: "))

    resultado = numero1 + numero2
   
    print(f"A soma de {numero1} + {numero2} é : {resultado}") 

somar()