# decomposição - dividir o problema em partes menores

salario_liq = 0

salario_bruto = 1200.00
inss = salario_bruto * 0.08
periculosidade = salario_bruto * 0.10

salario_liq = salario_bruto + periculosidade - inss
print('salario bruto:', salario_bruto)
print('inss:', inss)
print('periculosidade:', periculosidade)
print('Salário líquido:', salario_liq)