
numero= int(input("Digite um valor inteiro:"))
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print(f'Os divisores do {numero} são: {contador}')