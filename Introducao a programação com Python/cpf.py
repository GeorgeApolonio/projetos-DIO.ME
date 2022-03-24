
def validar_cpf(cpf):

    digitos_cpf = []
    multiplo = 10
    resultado1 = 0
    resultado2 = 0

    for i in cpf:
        digitos_cpf.append(int(i))

    for d in range(0, 9):
        resultado1 = resultado1 + (digitos_cpf[d] * multiplo)
        resultado2 = resultado2 + (digitos_cpf[d+1] * multiplo)
        multiplo -= 1

    resto1 = resultado1%11
    resto2 = resultado2%11

    if resto1 == 0 or resto1 == 1:
        digito_v1 = 0
    else:
        digito_v1 = 11 - resto1

    if resto2 == 0 or resto2 == 1:
        digito_v2 = 0
    else:
        digito_v2 = 11 - resto2

    if digito_v1 == digitos_cpf[9] and digito_v2 == digitos_cpf[10]:
        print('CPF válido.')
    else:
        print('CPF inválido.')


if __name__ == '__main__':
    validar_cpf('94767955572')