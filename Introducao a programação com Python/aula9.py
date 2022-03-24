#trabalhando com arquivos

arquivo = open('teste.txt', 'w') #se o arquivo nao existe ele cria no modo escrita (w)
arquivo.write('Primeira Linha') #escreve o texto, mais apaga - se ja existir - algo dentro
arquivo.close() #fecha o arquivo apos usa-lo

arquivo = open('teste.txt', 'a') #se o arquivo nao existe ele cria e faz append do texto
arquivo.write('\nSegunda Linha') #excreve o texto no final do existente dentro do arquivo
arquivo.close() #fecha o arquivo apos usa-lo


def criar(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')  # se o arquivo nao existe ele cria no modo escrita (w)
    arquivo.write(texto)  # escreve o texto, mais apaga - se ja existir - algo dentro
    arquivo.close()  # fecha o arquivo apos usa-lo

def atualizar(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')  # se o arquivo nao existe ele cria e faz append do texto
    arquivo.write(texto)  # excreve o texto no final do existente dentro do arquivo
    arquivo.close()  # fecha o arquivo apos usa-lo

def ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #abre o arquivo no modo leitura
    text = arquivo.read() #armazena o texto do arquivo
    print(text)

def copia(nome_arquivo):
    import shutil #utilizado para operações com arquivos
    shutil.copy(nome_arquivo, 'D:/A4NetTecnologias/A4NetSistemas/ProjetosDIO/arquivos')


def mover(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'D:/A4NetTecnologias/A4NetSistemas/ProjetosDIO/arquivos')


if __name__ == '__main__':
    #criar('teste.txt', 'George Apolonio.\n')
    #atualizar('teste.txt', 'Nubia Trindade\n')
    #atualizar('teste.txt', 'Jorge Felipe')
    #ler('teste.txt')

    #atualizar('aluno.txt', 'George,9,8,7,6\n')
    #atualizar('aluno.txt', 'Nubia,8,7,6,5\n')
    #atualizar('aluno.txt', 'Felipe,9,5,3,8')

    #ler('aluno.txt')
    arquivo = open('aluno.txt', 'r')
    texto = arquivo.read()
    print(texto)
    linhas = texto.split('\n') #pega cada linha do arquivo e armazena em uma lista - usa a quebra de linha como refeencia
    print(linhas)
    for x in linhas: #pega cada item da lista
        boletin = x.split(',') #cria cada aluno separando seus dados com base na '
        print(boletin)
        nome_aluno = boletin[0] #armazena só o nome do aluno
        boletin.pop(0) #tira do boletin o nome do aluno e mantem so as notas
        print(nome_aluno)
        print(boletin)
        media = lambda notas: sum([int(i) for i in notas]) / 4 #cria o metodo/variavel media, pega cada nota, soma e divide por 4 - notas e o parametro da funcao
        print(media(boletin)) #chama a função media/lambda utilizando os dados da variavel boletim, calcula, e imprime o resultado


copia('aluno.txt')