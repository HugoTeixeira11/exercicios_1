"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha
Exemplo da estrutura de armazenamento das vendas:
    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]
    ou então:
    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""

if __name__ == '__main__':
    ilhas = ['Terceira', 'Pico', 'Graciosa', 'Faial', 'São Jorge']
    tipos = ['Gasolina', 'Gasoleo']
    vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    while True :
        try:
            for x in range(len(tipos)):
                for y in range(len(ilhas)):
                    vendas[x][y] = int(input(f'Qual o número de vendas na ilha {ilhas[y]} e do tipo {tipos[x]}: '))
            print(vendas)

            #total de vendas e de vendas por tipo
            total_vendas = 0
            for x in range(len(tipos)):
                total_tipo = 0
                for y in range(len(ilhas)):
                    total_tipo += vendas[x][y]
                    total_vendas += vendas[x][y]
                print(f'Total de vendas de {tipos[x]} = {total_tipo}')
            print(f'Total de vendas = {total_vendas}')

            # total de vendas e de vendas por ilha
            for y in range(5):
                total = 0
                for x in range(2):
                    total += vendas[x][y]
                print(f'Total de vendas de {ilhas[y]} = {total}')
                break

        except ValueError:
            print(f'Insira um valor válido para vendas.')





            #for y in range(len(vendas[0])):
                #total_ilhas = 0
                #for x in range(len(vendas)):
                   # print(f'vendas[{x}][{y}]={vendas[x][y]}')
                   # total_ilhas += vendas[x][y]
              #  print(f'total de cada ilha = {total_ilhas}')



               # for y in range(vendas(5):
               # total_ilhas = 0
               # for x in range(vendas(2):
                  #  print(f'vendas[{x}][{y}]={vendas[x][y]}')
                 #   total_ilhas += vendas[x][y]
                #print(f'total de cada ilha = {total_ilhas}')





