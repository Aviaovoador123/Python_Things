num = int(input('Digite um numero:'))

uni = num %10
dez = (num // 10) % 10
cen = (num // 100) % 10
mil = (num // 1000) % 10

print('Unidade:', uni, '\nDezena:', dez, '\nCentena:', cen, '\nMilhar:', mil)