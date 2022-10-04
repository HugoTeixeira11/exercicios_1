"""
17. Dado um conjunto de n inteiros representando notas de alunos, escreva
um programa em Python para determinar quantos tiveram nota positiva.
Modifique o seu programa de modo a também calcular qual a percentagem
de notas positivas.
"""

if __name__ == '__main__':
    while True:
        try:
            notas = []
            num_alunos = int(input('Quantos alunos são: '))

            num_alunos_positivo = 0
            num_alunos_negativo = 0
            while num_alunos > 0:
                try:
                    num_alunos -= 1
                    notas.append(int(input('Insira a nota: ')))


                except ValueError:
                    num_alunos += 1
                    print(f'Insira um valor valido')

            print(notas)
            for x in range(len(notas)):
                if notas[x] >= 50:
                    num_alunos_positivo += 1
            print(f'Dos {len(notas)} alunos, {num_alunos_positivo} teve/tiveram positiva')
            percentagem_notas = (num_alunos_positivo * 100) / len(notas)
            print(f'Dos {len(notas)} alunos, {int(percentagem_notas)}% teve/tiveram positiva')

            continuar = input('Repetir (S | N')
            if continuar == 'N':
                break

        except ValueError:
            print('Insira um valor')