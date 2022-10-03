"""
7. Escreva um programa em Python que lê o número de horas, que um em-
pregado trabalhou numa dada semana e o seu salário/hora e calcula o

ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas fôr menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora, em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
"""




if __name__ == '__main__':
    horasFeitas = int(input(f'Quantidade de horas feitas: '))
    salario_horas = int(input(f'Salario por hora: '))
    while True:

            if horasFeitas > 40:
                diferenca = horasFeitas - 40
                pagamento = 40 * salario_horas
                extra = diferenca * (salario_horas * 2)
                pagamento = pagamento + extra
            print(f' O seu salario é {pagamento}')
            break