objetos = ('Lápis' , 'Borracha' , 'Caderno')
print(objetos[2]) #Irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos)) #irá mostrar o tipo de variável

print(objetos) #exibindo todos os itens de uma vez só

print("-"*50)
for item in range(0,3):
    print(objetos[item]) #exibindo todos os itens da tupla, em forma de lista (range)

#Exibindo todos os itens da tupla sem a função range
print("-"*50)
for elementos in objetos:
    print(elementos)

#Iremos tentar alterar o conteúdo da tupla
objetos[0] = "Caneta"