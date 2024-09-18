#Criando um dicionário, é basicamente uma lista com índice textual

pessoa = {
    'Nome': 'Maria',
    'Idade' : 20,
    'Endereço': 'Avenida 23'
}
print(pessoa)

#Exibindo as chaves utilizando o comando keys () (antes dos dois pontos)
print(pessoa.keys())

#Exibindo os valores utilizando o comando values () (depois dos dois pontos)
print(pessoa.values())

#Exibindo tanto a chave quanto o valor
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
#Realizando operações com dicionário 
#Adicionando dados 
#Forma 1
pessoa["Peso"] = 68
print(pessoa)

#Forma 2 - Usando update()
pessoa.update({"Profissão" : "Diretora"})

#Removendo dados do dicionário
#Forma 1 - pop()
pessoa.pop("Peso")
print(pessoa)

#Forma 2 - del()
del(pessoa["Endereço"])
print(pessoa)