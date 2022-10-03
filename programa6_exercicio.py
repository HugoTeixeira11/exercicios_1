"""
Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos.
"""

def maior(num1, mum2, num3):
    if num1 > num2 and num1 > num3:
        maior = num1
    if num2 > num1 and num2 > num3:
        maior = num2
    if num3 > num2 and num3 > num1:
        maior = num3
    return maior


if __name__ == '__main__':
    num1 = (int(input('Insira o primeiro num: ')))
    num2 = (int(input('insira o segundo num: ')))
    num3 = (int(input('Insira o terc num: ')))
    print(f'O maior numéro é {maior(num1,num2,num3)}')