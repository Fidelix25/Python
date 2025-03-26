# Calculadora simples
import operator


try:
    num1 = float(input("Primeiro Número: "))
    num2 = float(input("Segundo Número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/" and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
