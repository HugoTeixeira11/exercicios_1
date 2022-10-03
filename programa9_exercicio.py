"""9. Escreva um programa em Python que lê uma sequência de dígitos, sendo
cada um dos dígitos fornecido numa linha separada, e calcula o número
inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
sequência de dígitos é fornecido ao programa o inteiro

1. O seu programa

deve permitir a interação:
Escreva um dígito
(-1 para terminar)
? 3
Escreva um dígito
(-1 para terminar)
? 2
Escreva um dígito
(-1 para terminar)
? 5
Escreva um dígito
(-1 para terminar)
? 7
Escreva um dígito
(-1 para terminar)
? -1
O número é: 3257"""

if __name__ == '__main__':

    lista_nums = []

    while True:
        try:
            numeros = int(input('Escreve um digito: '))


            numeros = str(numeros)

            for x in range(len(numeros)):
                print(f'{numeros[x]}')

            if numeros == '-1':
                break

            lista_nums.append(numeros)


        except ValueError:
            print('Insira um valor valido')
    print(numeros)
    print(f'Força')
