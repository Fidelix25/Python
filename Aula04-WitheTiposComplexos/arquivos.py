import csv

caminhoArquivo = "exemplo.csv"

arquivoCSV = []

# Gerenciador de contexto, abri o arquivo, atua nele e depois o fecha, possibilitando que outros também o utilizem.
with open(caminhoArquivo, "r", encoding="utf_8") as arquivo:
    leitorCSV = csv.DictReader(arquivo)

    for linha in leitorCSV:
        arquivoCSV.append(linha)

print(arquivoCSV)
