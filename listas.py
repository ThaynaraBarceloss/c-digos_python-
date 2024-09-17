animais = ["Cachorro" , "Gato" , "Ovelha"]
print(type(animais)) #exibindo o tipo de variável

print(animais)

#Exibindo todos os itens da lista
print("-"*50)
for itens in animais:
    print(itens)

 #1ª etapa : atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2ª etapa: inserir dados
print("-"*50)
#Forma 1 - usando append
animais.append("Cavalo") #Irá inserir um novo item no final da lista
print(animais)

#2ª forma - usando insert
animais.insert(1, "Pássaro") #O insert precisa de 2 valores, o 1º será o índice que desejo inserir o valor.O 2º é o conteúdo que quero inserir na lista (inserir em qualquer lugar)
print(animais)

#3ª Etapa - Excluir dados
print("-"*50)
#Forma 1 - usando pop()
animais.pop() #Remove o último item da lista
print(animais)

#Forma 2- Usando pop() com índice
animais.pop(0) # Serve para escolher qual índice da lista será excluído
print(animais)

#Forma 3 - Usando remove
animais.remove("Ovelha") #irá remover o item pelo seu conteúdo
print(animais)