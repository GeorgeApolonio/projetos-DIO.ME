a = 10
b = 6
soma = a + b
sub = a - b
multi = a * b
divis = a / b
resto = a%b

print(type(soma))
print(soma, sub, multi, divis, resto)
print('soma é:', soma)
print('soma é: ' + str(soma))
print('soma é: {}'.format(soma))

anoatual = int(input('Entre com o ano atual: '))
anonasc = int(input('Entre com seu ano de nascimento: '))
idade = anoatual - anonasc

print('Você tem {} anos de idade.'.format(idade))