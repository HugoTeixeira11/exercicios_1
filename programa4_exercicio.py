"""
Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,

Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18
"""

def dias(valor1):
    dias = valor1 / 60  # segundos para minutos
    dias = dias / 60  # minutos para horas
    dias = dias / 24  # horas para dias

    return dias

def horas(valor1):
    horas = valor1 % (24 * 3600)
    horas = horas // 3600

    return horas

def minutos(valor1):
    minutos = valor1 % (24 * 60)
    minutos = minutos // 60

    return minutos

def segs(valor1):
    seg = valor1
    seg %= 60

    return seg

if __name__ == '__main__':
    segundos = int(input(f'Insira o valor em segundos: '))
    print(f'dias:{int(dias(segundos))} horas:{int(horas(segundos))} minutos: {int(minutos(segundos))} seg: {int(segs(segundos))} ')
