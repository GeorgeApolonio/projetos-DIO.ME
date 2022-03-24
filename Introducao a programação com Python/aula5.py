lista = [8, 3, 11, 7]
animais = ['gato', 'cachorro', 'elefante']

print(lista)
print(animais)
print(animais[1])

for i in lista:
    print(i)

if 'porco' in animais:
    print("voce tem esse animal")
else:
    print('voce nao tem esse animal na lista')
    animais.append('porco') #adicionar
    print('O animal foi incluido na lista')
    animais.remove('gato') #remove um item pelo nome
    animais.pop(0) #remove pela posicao

print(animais)

lista.sort() #ordena a-z
print(lista)
lista.reverse()
print(lista) #ordena z-a

tupla = (3, 11, 9, 2) #tupla nao pode ser modificada
print(tupla)

lista_tupla = tuple(lista)
print(lista_tupla)

tupla_lista = list(tupla)
print(tupla_lista)

