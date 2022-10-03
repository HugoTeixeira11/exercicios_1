"""
3. Escreva um programa em Python que pede ao utilizador que lhe forneça

um inteiro correspondente a um número de segundos e que calcula o nú-
mero de dias correspondentes a esse número de segundos. O seu programa

deve permitir a interação:
Escreva um número de segundos
? 65432998
O número de dias correspondentes é 757.3263657407407
"""

def segundosParaDias(valor1):

    valor1 = valor1 / 60 #segundos para minutos
    valor1 = valor1 / 60 #minutos para horas
    valor1 = valor1 / 24 #horas para dias
    return valor1

if __name__ == '__main__':
    segundos = int(input('Escreva o valor em segundos: '))
    print(f'{segundos} segundos em dias são {segundosParaDias(segundos)} dias.')
