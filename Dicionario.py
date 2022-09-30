"""
BI
Nome
Morada
Codigo Postal
Custo Hora xxx (float)
Ano Nascimnento xxx
"""
pessoas = (1, 'Maria', {'morada' : 'Rua de cima', 'cp' : 9500}, 12.50, [123,4234,123,542])

meses = {'Janeiro', 'Fevereiro', 'Março'}

if __name__ == '__main__':
    """Dicionario = {
        "Bi" : "19002132",
        "nome" : "Hugo Teixeira",
        "morada" : "Rua X",
        "codigo postal" : "9630-199",
        "custo hora" : 17.0,
        "ano nascimento" : 2004
    }
    print(pessoas[2].keys())
    print(pessoas[2].values())
    print()
    for k in pessoas[2].keys():
        print(k)
    print()
    for v in pessoas[2].values():
        print(v)
    print()
    for k in pessoas[2].keys():
        print(f'{k} = {pessoas[2][k]}')"""
    meses.add('Abril')
    print(meses)
    meses.pop()
    print(meses)

