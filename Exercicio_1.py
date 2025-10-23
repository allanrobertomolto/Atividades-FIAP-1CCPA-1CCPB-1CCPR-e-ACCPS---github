#Escreve Arquivo
compras = ["Arroz", "Feijão", "Macarrão", "Azeite", "Leite", "Pão", "Café"]

with open("minhas_compras.txt", "w", encoding="utf-8") as arquivo:
    for item in compras:    #Percorre cada item da lista
        arquivo.write(item + "\n")

print("Arquivo 'minhas_compras.txt' criado com sucesso!")


#Lê Arquivo
with open("minhas_compras.txt", "r", encoding="utf-8") as arquivo:
    print("Itens da lista de compras:\n")
    for linha in arquivo:
        print(linha.strip())
print("\nLeitura concluída com sucesso!")
