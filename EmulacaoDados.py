#Criando o arquivo
import random
import csv

ARQUIVO = "log_medidas.csv"  # nome do arquivo gerado
N = 20                       # quantidade de amostras

# Geração dos valores simulados
correntes = [round(random.uniform(0.5, 10.0), 2) for _ in range(N)]
tensoes = [round(random.uniform(110.0, 127.0), 2) for _ in range(N)]

# Escrita no arquivo CSV
with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f) #Cria o objeto que escreve no arquivo CSV
    writer.writerow(["Amostra", "Corrente (A)", "Tensão (V)"])
    for i in range(N):
        writer.writerow([i + 1, correntes[i], tensoes[i]])

print(f"Arquivo '{ARQUIVO}' gerado com sucesso!")

#Lendo o arquivo
import csv

with open("log_medidas.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(f"Amostra {linha['Amostra']}: {linha['Corrente (A)']} A, {linha['Tensão (V)']} V")
