#Custo da viagem
viagem = float(input('Qual a distância da viagem?'))
preco1 = viagem * 0.50
preco2 = viagem * 0.45
if viagem <= 200:
    print('O preço de sua passagem é de R${:.2f}'.format(preco1))
else:
    print('O preço de sua passagem é promocional e custará R${:.2f}'.format(preco2))
