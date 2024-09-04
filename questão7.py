produto = float(input("Informe o valor do produto:"))
pagamento= int(input("Digite 1 se o seu pagamento for avista (pix,débito ou dinheiro)\n Digite 2 se se o pagamento for no cartão de crédito\n Digite 3 se o pagamento for em duas vezes, preço normal sem juros\n Digite 4 em três vezes, preço normal mais juros de 10%:"))

pagamento1 = produto * 0.85 
pagamento2 = produto * 0.10
pagamento4 = produto * 1.10 

if pagamento == 1:
    print(f"O valor total da compra foi: {pagamento1}")
elif pagamento == 2:
    print(f"O valor total da compra foi: {pagamento2}")
elif pagamento == 3:
    print(f"O valor total da compra foi {produto}")
elif pagamento == 4:
    print(f"O valor total da compra foi: {pagamento4}")