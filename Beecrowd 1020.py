# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, coo 360, 363 ou 364.

diastotal = int(input())
ano = int(diastotal/365)
meses = int((diastotal % 365)/30)
dias = int((diastotal % 365) % 30)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
