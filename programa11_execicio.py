"""
11. Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""

if __name__ == '__main__':

    while True:
        try:
            numero = int(input(f'Insira um numero: '))
            numero = str(numero)
            print(f'O numero invertivo é {numero[::-1]}')
            break
        except ValueError:
            print(f'Insere num numero')
