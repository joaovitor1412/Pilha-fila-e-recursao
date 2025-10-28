#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

entrada_de_genero = input("escreva genero (f)-feminino (M)-masculino (O)-otros")
if entrada_de_genero == "f":
    print(f"seu genero{entrada_de_genero} É feminino")
elif   entrada_de_genero == "M":
  print(f"seu genero{entrada_de_genero} É masculino")  
elif entrada_de_genero == "O":
   print(f"seu genero{entrada_de_genero} no indetificado")
else:
   print("entrada não é valido por favor escreva (f) (M) ou (O)")
