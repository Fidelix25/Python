# loop For
for i in range(1, 5):
    print(i)

alunos = ["Rafael", "Fabio", "Luciano"]

for aluno in alunos:
    print(aluno)

texto = "Hoje é nossa Terceira Aula do Bootcamp, Bootcamp de Python"
novo_texto = texto.replace(",", "")
palavras = novo_texto.split(" ")
print(palavras)

contagem_palavras = {}
# Percorrer todas as palavras dentro da lista de palavras e checar se ela já está no dicionário contagem de palavras
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
