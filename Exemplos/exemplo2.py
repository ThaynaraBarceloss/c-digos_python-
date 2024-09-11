nome = "Thaynara Barcelos"
end = "Avenida castelo branco"
idade = "17 anos"

# print (nome, end, idade)
# 1 ª forma de concatenação
print ("Olá,",nome, "seu endereço é " , end,  "sua idade é " , idade)

#2 ª forma de concatenação 
print("Seja bem vindo {} sua residência está na {} e você possui {} ".format (nome,end,idade))

#3ª forma de concatenação f-string
print(f"Olá, seja bem vindo {nome}, o seu endereço é {end} e sua idade é {idade}")