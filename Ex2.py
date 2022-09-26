"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""


if __name__ == '__main__':
    vogais_count = 0
    vogais = set('aeiouAEIOU')
    continuar = 's'
    while continuar == 's':
        frase = str(input('Insira uma frase: '))
        nl = frase.split(' ')
        print(f'A frase tem {len(nl)} palavras')
        for char in frase:
            if char in vogais:
                vogais_count += 1
        print(f'A frase tem {vogais_count} vogais')
        continuar = input('Repetir [s | n] ? ')
    print(f'Adeus!')