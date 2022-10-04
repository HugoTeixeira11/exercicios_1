def digitos(numero):
    numero = str(numero)
    digito = 0
    for x in range(len(numero)):
        digito += int(numero[x])
    return digito
if __name__ == '__main__':
    numero1 = int(input(f'Insira um numero'))


    print(f'O a soma dos digitos de {numero1} é {digitos(numero1)}')