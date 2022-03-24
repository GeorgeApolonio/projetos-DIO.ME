#modulo - arquivos py

import aula7
from aula7 import Televisao
from aula7 import contador_letras

if __name__ == '__main__':
    tv = Televisao()
    print('a Tv está ligada?', tv.ligada)
    tv.power()
    print('a tv está ligada?', tv.ligada)
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)
    tv.aumenta_vol()
    print('Volume:', tv.volume)

    lista = ['george', 'nubia', 'felipe']
    print(contador_letras(lista))



#lambda - é uma função anônima - simplificar algo que é repetido

#metodo e consulta normal para contar letras
def contador_letras(lista_palavra): #contar letras de cada palavra da lista
    quantidade = [] #vai armazenar a quanditade de letra de cada palavra
    for x in lista_palavra: #x armazena cada palavra da lista por vez
        contador = len(x) #armazena letras contadas da palavra
        quantidade.append(contador) #adiciona a quant letras da palavra contada nessa lista
    return quantidade #retorna a lista das quantidades de letras

lista = ['george', 'nubia', 'felipe']
print(contador_letras(lista))

#metodo usando lambda para contar letras
contador_letra = lambda lista: [len(x) for x in lista] #criou uma variavel/metodo contador_letra

lista_sand = ['pao', 'queijo', 'manteiga'] #gerou a lista
print(contador_letra(lista_sand)) #chamou e imprimiu a variavel/metodo baseado na lista especificada

#outro exemplo
soma = lambda a, b: a + b #criou a variavel/metodo soma com dois parametros e a operacao a ser executada
print(soma(3, 5)) #chama e imprime a soma com base nos parametros