nome= (input("Informe o seu nome:"))
sexo= (input("Informe o seu sexo:"))
civil= (input("Informe o seu estado civil:"))

if sexo == "feminino" and  civil =="casada":
    tempo = (input("Quanto tempo de casada?"))
    print(f"Seu nome é,{nome}, você tem {tempo} de casada")

else :
    print(f"Obrigado {nome} , até a próxima!") 
