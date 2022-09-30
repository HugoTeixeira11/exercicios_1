def fatorial(num):
    total = 1
    for x in range(1, num + 1):
        total *= num
        num -= 1
    return total


if __name__ == '__main__':
    while True:
        num = int(input('Insira um numero: '))
        print(fatorial(num))

