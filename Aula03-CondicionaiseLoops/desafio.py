### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
dicionario = {}

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is not True:
    try:
        nome: str = input("Digite seu nome: ")
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio")
        elif nome.isdigit():
            raise ValueError("O nome não deve conter números.")
        else:
            nome_valido = True
            print("Nome válido:", nome)
    except ValueError as e:
        print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while salario_valido is not True:
    try:
        salario: float = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salario")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário")

# 3) Solicita ao usuário que digite o valor do bônus recebido
while bonus_valido is not True:
    try:
        bonus: float = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0.0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número")

# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

bonus_recebido: float = round(1000 + salario * float(bonus), 3)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu salário é de R${salario} e seu bônus final é R${bonus_recebido}")

dicionario.update(
    {"nome": nome, "salario": salario, "bonus": bonus, "bonus_recebido": bonus_recebido}
)

print(dicionario)
