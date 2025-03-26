# Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().
numero = 10.57
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

# # Exemplo que causa TypeError
# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro

# Type conversion
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

# Exemplo try-except
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")

# Exemplo com if
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")
