# Controle de Fluxo
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

print(x)

# Garantir que preços e quantidades não estejam negativos

quantidade = 40
preco = -20

if quantidade > 0 and preco > 0:
    print("Valores Válidos")
else:
    print("Valores inválidos")
