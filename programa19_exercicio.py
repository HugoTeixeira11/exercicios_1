"""
19. Escreva um programa em Python que lê uma quantia em Euros e calcula
o número de notas de 50 e, 20 e, 10 e, 5 e e moedas de 2 e, 1 e, 50
cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos e 1 cêntimo,
necessário para perfazer, essa quantia, utilizando sempre o máximo nú-
mero de notas e moedas para cada quantia, da mais elevada, para a mais
baixa.
"""

if __name__ == '__main__':
    while True:
        try:
            quantia = input('Qual é a quantidade em euros? ')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')