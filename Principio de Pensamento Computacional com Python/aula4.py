# padrões - identificar situações que já ocorreram se repetiram durante os processo

lista = {"arroz": 3.50, "feijao": 6.60, "carne": 35.00}


valor_disponivel = 10.00

for i in lista:
    if lista[i] <= valor_disponivel:
        print('Pode comprar {}'.format(i))
    else:
        print('Não pode comprar {}.'.format(i))