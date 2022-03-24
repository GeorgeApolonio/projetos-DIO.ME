
#vai tentar dividir por 0 - como não pode então vai gerar a excessaõ
try:
    divisao = 10 / 0
except ZeroDivisionError:
    print('Não é possível dividir por zero.')

# vai tentar acessar um indice da lista que não existe
lista = 1, 10
try:
    numero = lista[3]
except IndexError:
    print('A lista não tem o índice 3')

#toda excessão tem pi i filho - o BaseException é o pai de todas que existem

#vai tentar armazenar o valor de a no x
#como o "a" não existe, vai gerar uma exceção.
#já que não sabemos qual o tipo de exceção, ele vai armazenar
#na variavel "ex" o erro ocorrido e exibir na tela.
try:
    x = a
except BaseException as ex:
    print('Erro desconhecido. O erro é: {}'.format(ex))

#se for uzar excessão encadeada, tem que observar
#a arvore hierarquica para evitar erros de logica

#se não ocorrer erro de exceção ele executa o else
try:
    x = 1
except BaseException as ex:
    print(ex)
else:
    print('Deu tudo certo.')

#se dendro do "try" tiver várias linhas que podem ou não
#gerar exceção, quando ocorrer a primeira exceção,
#as demais linhas serão enterrompidas
#então se tiver algo que queira que seja executado
#mesmo que ocorra erro, deve ser colocado no "finally"

try:
    divisao = 10 / 0
    x = a
    x = 1
    numero = lista[3]
except IndexError:
    print('A lista não tem o índice 3')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except BaseException as ex:
    print('Erro desconhecido. O erro é: {}'.format(ex))
else:
    print('Será que deu tudo certo.')
finally:
    print('Deu tudo certo sim.')

#personalizar ou criar uma exceção
#primeiro cria uma classe que herde de Exception
class Error(Exception):
    pass

#depois cria a classe personalizad que herde da anterior
class InputError(Error):
    def __init__(self, menssagem): #construtor
        self.mensage = menssagem



while True: #enquanto for verdade fic repetindo
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #dessa forma que se chama uma exceção personalizada - com raise
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break # se o try der certo ele cancela o while
    except ValueError:
        print('Valor invalido. Tente novamente.')
    except InputError as ex:
        print(ex)
