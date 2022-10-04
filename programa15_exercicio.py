"""
15. Escreva um programa que lê uma série de dígitos (terminando com -1) e
calcula o inteiro que tem esses dígitos. Por exemplo, lendo os dígitos 1 5
4 5 8 -1, calcula o número inteiro 15458.
"""
if __name__ == '__main__':

    lista_nums = []

    while True:
        try:
            numeros = int(input('Escreve um digito: '))

            if numeros < 0:
                break

            lista_nums.append(numeros)


        except ValueError:
            print('Insira um valor valido')


    numeros = ''
    for x in range(len(lista_nums)):
        numeros += str(lista_nums[x])


    print()
    print(f'Força')
