entrada = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros: ", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros")
