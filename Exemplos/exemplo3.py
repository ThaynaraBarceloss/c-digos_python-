nota1 = float (input ("Informe a 1ª nota: ")) #input serve para pedir informações para os usuários/estamos convertendo os valores textuais em valores decimais.
nota2 = float (input ("Informe a 2ª nota: "))
nota3 = float (input ("Informe a 3ª nota: "))

media = (nota1+nota2+nota3)/3

print(f"Sua média é {media:.2f}") #.2f significa que teremos 2 casas decimais após a vírgula.