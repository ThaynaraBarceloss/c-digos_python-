valorA =  int(input("Informe o valor de A: "))
valorB = int(input("Informe o valor de B: "))

if valorA == valorB :
    valorC = valorA + valorB
    print(f"O {valorA} , é igual ao o {valorB}, logo a soma do valor A mais o valor B é igual a {valorC}")

elif valorA != valorB:
    valorC = valorA* valorB 
    print(f"O {valorA} , é diferente do {valorB}, logo a multiplicação do valor A vezes o valor B é igual a {valorC}")