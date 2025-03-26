# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("digite a data no formato 'dd/mm/yyyy': ")
# listaData = data.split("/")
# print("Dia: " + listaData[0])
# print("Mês: " + listaData[1])
# print("Ano: " + listaData[2])

data = input("digite a data no formato 'dd/mm/yyyy': ")
dia, mes, ano = data.split("/")
print("Dia: " + dia)
print("Mês: " + mes)
print("Ano: " + ano)
