### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
temperatura = int(input("Digite a temperatura: "))

if temperatura < 18:
    print("temperatura baixa")
elif 18 <= temperatura < 23:
    print("temperatura Normal")
else:
    print("temperatura alta")
