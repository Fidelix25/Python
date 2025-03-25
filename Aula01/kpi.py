# O programa deve começar solicitando ao usuário que insira seu nome.
userName = input("Digite o seu nome: ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
userSalary = float(input("Digite o seu salário: "))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonusPercentage = float(input("Digite o percentual do bônus: "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
adicionalBonus = 1000
bonusKPI = adicionalBonus + userSalary * bonusPercentage

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {userName}, o seu bônus foi de {bonusKPI}")

# Exemplo de Saída:
# Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:
