"""
Objetivo: Aprender tomada de decisão - (IF)"""



numero = int(input("Digite um numero: "))

if numero > 0:
    print("Numero é positivo.")
elif numero < 0:
    print("Numero é negativo.")
else:
    print("Numero é ZERO")

print("\n*******Maior ou Menor de idade**********")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Parabens, voce ja é um Adulto.")
else:
    print("Voce ainda é menor de idade.")
