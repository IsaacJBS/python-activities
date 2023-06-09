# Define a função dimensoesObjeto() que recebe as dimensões de um objeto e retorna o
# valor do frete de acordo com a tabela abaixo:
def dimensoesObjeto():
    while True:
        try:
            comprimento = int(input('Digite o comprimento do objeto (em cm):'))
            largura = int(input('Digite a largura do objeto (em cm):'))
            altura = int(input('Digite a altura do objeto (em cm):'))
            volume = float(comprimento * largura * altura)
            print('O Volume calculado do objeto é: {:.2f}Cm³'.format(volume))
            if volume < 1000:
                return 10.00
            elif 1000 <= volume < 10000:
                return 20.00
            elif 10000 <= volume < 30000:
                return 30.00
            elif 30000 <= volume < 100000:
                return 50.00
            else:
                print('*Objeto fora do tamanho o aceitável! \n' 'Por favor, entre com as dimensões novamente')
                continue
        except ValueError:
            print('*Valor informado não é numérico! \n' 'Por favor, entre com as dimensões novamente')
            continue


# Define a função pesoObjeto() que recebe o peso de um objeto e retorna o valor do frete
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg):'))
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print('Objeto acima do peso acitável!')
                continue
        except ValueError:
            print('Valor digitado não numérico \n' 'Entre com o peso desejado novamente')
            continue


# Define a função rotaObjeto() que recebe a rota de um objeto e retorna o valor do frete
def rotaObjeto():
    while True:
        try:
            rota = (input('Selecione a rota: \n'
                          'RS - De Rio de Janeiro até São Paulo \n'
                          'SR - De São Paulo até Rio de Janeiro \n'
                          'BS - De Brasília até São Paulo \n'
                          'SB - De São Paulo até Brasília \n'
                          'BR - De Brasília até Rio de Janeiro \n'
                          'RB - Rio de Janeiro até Brasília \n>>'))
            if rota.lower() == 'rs':
                return 1
            elif rota.lower() == 'sr':
                return 1
            elif rota.lower() == 'bs':
                return 1.2
            elif rota.lower() == 'sb':
                return 1.2
            elif rota.lower() == 'br':
                return 1.5
            elif rota.lower() == 'rb':
                return 1.5
            else:
                print('*Código de Rota inexistente!')
                continue
        except ValueError:
            print('*Código de Rota inexistente! \n' 'Por favor entre com a rota desejada novamente')
            continue


# Inicio do programa
print('Bem vindo a companhia de logistica Isaac Jordao Brito Santos S.A')
area = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
valor = (area * peso * rota)
print('Total a pagar: R$ {:.2f} - (Dimensões: {} * Peso: {} * Rota:{})'.format(valor, area, peso, rota))
