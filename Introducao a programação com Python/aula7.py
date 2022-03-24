#metodo - não retorna valor
def soma(a, b):
    resultado = a + b

#função - retorna valor
def soma(a, b):
    resultado = a + b
    return resultado

def subracao(a, b):
    resultado = a - b
    return resultado

def multiplicacao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    resultado = a / b
    return resultado

def contador_letras(lista_palavra): #contar letras de cada palavra da lista
    quantidade = [] #vai armazenar a quanditade de letra de cada palavra
    for x in lista_palavra: #x armazena cada palavra da lista por vez
        contador = len(x) #armazena letras contadas da palavra
        quantidade.append(contador) #adiciona a quant letras da palavra contada nessa lista
    return quantidade #retorna a lista das quantidades de letras


print(soma(1, 2))
print(subracao(5, 3))
print(multiplicacao(10, 7))
print(divisao(25, 5))


#Classe

class Calc1:
    def __init__(self, num1, num2): #funciona como um construtor da classe
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        resultado = self.num1 + self.num2
        return resultado

    def subracao(self):
        resultado = self.num1 - self.num2
        return resultado

    def multiplicacao(self):
        resultado = self.num1 * self.num2
        return resultado

    def divisao(self):
        resultado = self.num1 / self.num2
        return resultado

calculadora1 = Calc1(10, 2)
print('----------------------------')
print(calculadora1.num1)
print(calculadora1.num2)
print('----------------------------')
print(calculadora1.soma())
print(calculadora1.subracao())
print(calculadora1.multiplicacao())
print(calculadora1.divisao())


class Calc2:
    def __init__(self): #funciona como um construtor da classe
        pass #sem função - so para nao ficar vazio

    def soma(self, num1, num2):
        resultado = num1 + num2
        return resultado

    def subracao(self, num1, num2):
        resultado = num1 - num2
        return resultado

    def multiplicacao(self, num1, num2):
        resultado = num1 * num2
        return resultado

    def divisao(self, num1, num2):
        resultado = num1 / num2
        return resultado

calculadora2 = Calc2()
print('----------------------------')
print(calculadora2.soma(10, 2))
print(calculadora2.subracao(10, 2))
print(calculadora2.multiplicacao(10, 2))
print(calculadora2.divisao(10, 2))


class Televisao:
    def __init__(self):
        self.ligada = False
        self.volume = 5

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_vol(self):
        if self.volume < 10:
            self.volume += 1

    def diminui_vol(self):
        if self.volume > 0:
            self.volume -= 1


if __name__ == '__main__': #só executa o codigo abaixo se rodar este arquivo
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