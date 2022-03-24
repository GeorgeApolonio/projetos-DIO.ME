a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O maior valor é:', a)
elif a < b:
    print('O maior valor é:', b)
else:
    print('Os valores são iguais.')
print('Você conseguiu!')

if a%2 == 0:
    print('O numero {} é par.'.format(a))

if a%2 == 0 and b%2 == 0:
    print('Os números digitados foram par.')
elif a%2 != 0 and b%2 != 0:
    print('Os números digitados foram ímpares.')
else:
    print('Um número foi par e outro foi ímpar.')