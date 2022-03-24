from datetime import date, time, datetime, timedelta

dataatual = date.today()
print(dataatual)
print(dataatual.strftime('%d/%m/%y')) #pega a dat atul e converte par uma strind no formado basileiro dia/mes/ano
print(dataatual.strftime('%d/%m/%Y')) #fica ano com 4 digitos


horaatual = time(hour=23, minute=34, second=0) #cria um relogio com a hora especificda
print(horaatual)


datahora = datetime.now()
print(datahora)
print(datahora.strftime('%H:%M:%S  %d-%m-%Y'))
print(datahora.strftime('%c'))
print(datahora.day)
print(datahora.weekday()) #dia da semana em formato de numero
dias = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
print(dias[datahora.weekday()]) #pega o numero do dia da semna e localiza na tupla dias o item da posicao escolhida

datastring = '01/01/1976'
datareal = datetime.strptime('01/01/1976', '%d/%m/%Y')
print(datareal)


novadata = datareal - timedelta(days=50) #gera a data atual diminuindo 50 dias
print(novadata)