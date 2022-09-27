"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
"""

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']


if __name__ == '__main__':
    vendas = []
    for ilha in ilhas:
        vendas.append((int(input(f'Insira as vendas para {ilha} '))))
    print(f'vendas={vendas}')
    print(f'A soma das vendas das ilhas são: {sum(vendas)}')
    print(f'A media das vendas das ilhas são: {sum(vendas) / len(vendas)}')

    menor = vendas[0]
    maior = vendas[0]
    comprimento_ilhas = 0

    for x in range(1, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
        if vendas[x] > maior:
            maior = vendas[x]
    for x in vendas:
        if x == menor:
            print(f'O menor valor de vendas foi {menor} de {ilhas[comprimento_ilhas]}')
        if x == maior:
            print(f'O maior valor de vendas foi {maior} de {ilhas[comprimento_ilhas]}')
        comprimento_ilhas += 1
