### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

items = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(items):
    if items[i] == "parar":
        print("Parada encontrada, encerrando o processamento")
        break
    # Processa o item
    print(f"processando item: {items[i]}")
    i += 1
