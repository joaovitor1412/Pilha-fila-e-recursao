#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
Valor_1 = float(input("escreva um número:"))
print("Erro: escreva um numero com valor valido")
if Valor_1 > 0:
    print(f"o valor {Valor_1} É positivo.")
elif  Valor_1 < 0:
    print(f"o valor {Valor_1} É negativo.")
else:
    print(f"o valor é igual a 0")
