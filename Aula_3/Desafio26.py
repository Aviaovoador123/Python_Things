frase = str(input('Digite algo:'))
contar = frase.count('A')
priPos = frase.index('A')
ultPos = frase.rindex('A')

print(contar)
print('A letra a aparece pela primeira vez:', priPos)
print('A letra a aparece pela ultima vez:', ultPos)