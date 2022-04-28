n1=float(input('Qual o preço do produto? R$ '))
pro = n1*5/100
des = n1-pro
print('o preço do produto que é {:.2f}, na promoção com 5% de desconto fica: {:.2f}'.format(n1, des))