#def comfor(num1, num2):
    #for x in range(num1+1, num2+1):
        #inicio = num1
        #fim = num2
       # total = sum(range(num1, num2+1))
        #print(f'A soma é {total}')
        #break

def comfor(num1, num2):
    total = 0
    for x in range(num1, num2+1):
        total += x
    return total

def comwhile(num1, num2):
        total = 0
        while num1 < num2:
            total += num1
            num1 += 1
            if num1 == num2:
                break
        return total

#while num1 + num2:
     #   total = sum(range(num1, num2+1))
      #  print(f'A soma é {total}')
       # break

if __name__ == '__main__':
    while True:
        try:
            num1 = int(input('Insira o primeiro numero '))
            num2 = int(input('Insira o segundo numero '))
            if num2 < num1:
                print('O segundo tem ser maior que o primeiro ')
                break
            opçao = int(input('Quer fazer com um FOR ou WHILE ? [For - 1, while - 2] '))
            if opçao == 1:
                print(comfor(num1, num2))
            if opçao == 2:
                num2 += 1
                print(comwhile(num1, num2))
        except ValueError:
            print('Tem de inserir um numero!')

