total = 0

while True:
    
    valor = int(input("Digite um valor inteiro: "))

    if  valor >= 10 and valor <=100:
      total = valor * valor
      print(f"O quadrado do número é: {total}")
      
    elif valor >= 5 and valor < 10:
      total = valor * valor * valor
      print(f"O cubo do número é {total}")
      
    elif valor > 100:
      print("Limite excedido")
      break
        
    elif valor <= 0:
      print("Programa finalizado!")
      break