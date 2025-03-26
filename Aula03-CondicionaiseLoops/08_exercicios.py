### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
usuarios_invalidos = [usuario for usuario in usuarios if not usuario["email"]]

print(usuarios_validos)
print(usuarios_invalidos)
