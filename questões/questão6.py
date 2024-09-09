valorA =  int(input("Informe o valor de A: "))
valorB =  int(input("Informe o valor de B: "))
valorC =  int(input("Informe o valor de C: "))

if valorA > valorB and valorB > valorC:
    print(f"Ordem: {valorC}, {valorB} e {valorA}")

elif valorB > valorC> valorA:
        print(f"Ordem:{valorA}, {valorC}, {valorB}")
elif valorC > valorA > valorB:
        print(f"Ordem:{valorB}, {valorA}, {valorC}")