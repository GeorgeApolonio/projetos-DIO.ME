# pip --version -> mostra a versão do python
# pip --help -> mostra a lista de comandos
# pip list -> mostra os pacotes vieram instalados
# pip freeze -> mostra os pacotes que eu instalei

# módulos são os arquivos .py
# pastas que armazenam os modulos em comum
# pacotes/bibliotecas é o conjunto de pastas com modulos do que foi desenvolvido

# pip install requests -> instalando o pacote REQUESTS HTTP

import requests

# vai armazenar na variavel o site pego (get) pelo requests
response = requests.get('https://viacep.com.br/ws/01001000/json/')

# imprimi o codigo http (ex: 400 é codigo de erro do http)
print(response.status_code)

# imprime o conteudo do site em formato de lista
print(response.text)
print(type(response.text))

#imprime o conteudo do site em formato dicionário
#dessa forma é possivel manipular os dados por categoria (por bairro, por exemplo)
print(response.json())
print(type(response.json()))
dados = response.json() #armazena os dados na variavel em formato dicionario
print(dados['bairro']) #vai imprmir o bairro


# fazendo uma função para que o usuario escolha o cep
def consulta_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))
    dados = response.json()
    print(dados['localidade'])

def html_site(url): #pega o html de um site
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    cep = input('Digite o cep de sua cidade. Ex: 00000000.: ')
    consulta_cep(cep)

    #determina o site e imprime o seu html
    site = html_site('http://tilt.net/ztilt/index.php')
    print(site)