conjunto = {1, 2, 3, 4}
print(type(conjunto))
print(conjunto)

# conjunto não considera dados duplicados no seu conteudo
conj = {1, 2, 5, 5, 5, 3, 7}
print(conj)
conj.add(6) #adiciona elemento
print(conj)
conj.discard(5) #remove elemento
print(conj)

conjunto2 = {4, 9, 10, 11, 12}
uniao = conjunto.union(conjunto2) #a uniao remove as duplicidades
print(uniao)

intersecao = conjunto.intersection(conjunto2)
print(intersecao)

diferenca1 = conjunto.difference(conjunto2) #tem no conjunto e nao no conjunto2
diferenca2 = conjunto2.difference(conjunto) #tem no conjunto2 e nao no conjunto
print(diferenca1)
print(diferenca2)

simetrica = conjunto.symmetric_difference(conjunto2) #elimina o que tem igual nos dois ou seja, a intercesao
print(simetrica)

#subconjunto de um conjunto
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
conjsubset = a.issubset(b) #a é subconjunto do b - True - está contido em b
print(conjsubset)
conjsubset = b.issubset(a) #b é subconjunto de a - False
print(conjsubset)

conjsuperset = a.issuperset(b) #a é um super conjunto de b - False
print(conjsuperset)
conjsuperset = b.issuperset(a) #b é um super conjunto de a - True - contem a
print(conjsuperset)

lista = ['cachorro', 'cachorro', 'gato', 'elefante']
conjanim = set(lista) # converte lista em conjunto - elimina os repetidos
print(conjanim)
