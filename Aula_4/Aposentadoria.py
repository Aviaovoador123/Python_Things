idade = int(input('Digite sua idade: '))
tempCont = int(input('Digite seu tempo de contribuicao: '))

if idade >= 65 or tempCont >= 30:
    print('Voce pode se aposentar!')
else:
    print('Voce ainda nao pode se aposentar!')