#Faça um programa que verifique se uma letra digitada é vogal ou consoante.
vogal_ou_consoante = input("escreva uma letra")
if vogal_ou_consoante != "a,e,i,o,u":
    print(f" seu letra{vogal_ou_consoante} É uma vogal.")
elif  vogal_ou_consoante != "B, C, D, F, G, H, J, K, L, M, N, ç, P, Q, R, S, T, V, W, X, Y, Z. ":
    print(f"seu letra {vogal_ou_consoante} É uma consoante.")
else:
    print(f"por favor escreva um caracter valido")
    
