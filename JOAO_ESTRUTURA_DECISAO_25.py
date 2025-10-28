#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
número_1 =float(input("escreva número_1: "))
número_2 = float(input("escreva número_2: "))

media = (número_1 + número_2 ) /2
print(f"media {media}")

if número_1 > 7:
    print(f" Aprovado {número_1} se a média alcançada for maior ou igual a sete.")
if  número_2 < 7:
    print(f" Reprovado {número_2} se a média for menor do que sete.")
