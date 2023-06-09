import pandas as pd

dados = [
    [100, "Cachorro-quente", "R$ 9,00"],
    [101, "Cachorro-Quente Duplo", "R$ 11,00"],
    [102, "X-Egg", "R$ 12,00"],
    [103, "X-Salada", "R$ 13,00"],
    [104, "X-Bacon", "R$ 15,00"],
    [105, "X-Tudo", "R$ 17,00"],
    [200, "Refrigerante Lata ", "R$ 5,00"],
    [201, "Chá Gelado", "R$ 4,00"],
]

# Cabeçalho da tabela
cabecalho = ["Código", "Descrição", "Valor(R$)"]

# Criar um DataFrame do Pandas
df = pd.DataFrame(dados, columns=cabecalho)

# Imprimir tabela
print('Bem vindo a Lanchonete do Isaac Jordao')
print(16*"*", "Cardápio", 16*"*")
print(df)

#printa uma quebra de linha
print()

valor_total = 0
while True:
    codigo_informado = int(input("Entre com o código do produto: "))
    #se o código informad não estiver na lista, printa opção inválida
    if codigo_informado not in df["Código"].values:
        print("Opção inválida!")
        continue

    for item in dados:
        codigo = item[0]
        descricao = item[1]
        valor = item[2]

        if codigo == codigo_informado:
            print(f"Você pediu um {descricao} no valor de {valor}.")
            #adicina o valor unitário ao valor total
            valor_total += float(valor.replace("R$ ", "").replace(",", "."))
            break

    continuar = int(input("Deseja pedir mais alguma coisa? \n 0 - Não \n 1 - Sim "))
    
    if continuar == 0:
        print(f"O valor total a ser pago é: {valor_total:.2f}")
        break
