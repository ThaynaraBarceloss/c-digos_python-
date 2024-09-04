valor = int(input("Informe um valor numérico: "))

if valor>=20:
    print(f"O numéro {valor} é maior que 20 \n") #if = se for verdadeiro
elif  valor>= 10 and valor<=20: #else e if juntos 
    print(f"O número {valor} está entre 10 e 20\n")
else:
    print(f"O nuúmero {valor} é menor que 10 \n") # else: se não -> \n serve para quebrar a linha