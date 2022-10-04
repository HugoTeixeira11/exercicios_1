"""
18. Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos
"""

def contarZeros(numero):
    zeros = 0
    while numero % 10 == 0:
        zeros += 1
        numero /= 10
    return zeros

if __name__ == '__main__':
    while True:
        try:
            numero = int(input(f'Insira um numero: '))
            print(f'O numero {numero} tem {contarZeros(numero)} zeros')
        except ValueError:
            print(f'Insira Valores validos')

        continuar = input('Repetir ? (S | N)')
        if continuar == 'N':
            break
