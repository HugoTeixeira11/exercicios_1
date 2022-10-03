def media_KM(valor1, valor2):
    valor2 = valor2 / 60
    media = valor1 / valor2

    return media

def media_Ms(valor1, valor2):
    valor1 = valor2 / 1000
    valor2 = valor2 * 60
    media = valor1 / valor2
    return media

if __name__ == '__main__':
    valorKM = int(input('Insira o valor percorrido em KM: '))
    tempoPercorrido = int(input('Insira o tempo necessario em Minutos: '))
    print(f'{media_KM(valorKM, tempoPercorrido)}')
    print(f'{media_Ms(valorKM, tempoPercorrido)}')

