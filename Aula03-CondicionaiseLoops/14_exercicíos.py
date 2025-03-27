### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if tentativa == 4:  # Suponha que a conexão foi bem sucedida na quarta tentativa
        print("conexão bem-sucedida")
        break
    elif tentativa < 5:
        tentativa += 1
    else:
        print("Falha ao conectar após várias tentativas")
        break
