print('Bem vindo a Loja do Isaac Jordao')
# pega o valor unitário do produto
valor_unitario = float(input('Entre com o valor do produto: '))
# pega a quantidade do produto
quantidade = int(input('Entre com a quantidade do produto: '))

#printa o valor total sem desconto
valor_total = valor_unitario * quantidade
print('O valor sem desconto é: ', valor_total)

#printa o valor total com desconto caso haja
if quantidade < 10:
    print(f"O valor total com desconto é: {valor_total:.2f} (Não há desconto)")
elif 10 <= quantidade < 100:
    desconto = 0.05
    valor_do_desconto = valor_total * desconto
    valor_total = valor_total - valor_do_desconto
    print(f"O valor total com desconto é: {valor_total:.2f} (Desconto de 5%)")
elif 100 <= quantidade < 1000:
    desconto = 0.10
    valor_do_desconto = valor_total * desconto
    valor_total = valor_total - valor_do_desconto
    print(f"O valor total com desconto é: {valor_total:.2f} (Desconto de 10%)")
else:
    desconto = 0.15
    valor_do_desconto = valor_total * desconto
    valor_total = valor_total - valor_do_desconto
    print(f"O valor total com desconto é: {valor_total:.2f} (Desconto de 15%)")
