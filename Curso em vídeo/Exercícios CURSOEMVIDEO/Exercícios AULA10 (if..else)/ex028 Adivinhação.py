#Escolha um número
from random import randint
from time import sleep

print('========================================================')
print(' Tente adivinhar qual número o computador está pensando ')
print('========================================================')
n1 = int(input('Escolha um número entre 0 e 5 e : '))
print('PROCESSANDO...')
sleep(2)
n2 = randint(0, 5)
if n2 == n1:
    print('O número é {}'.format(n2))
    print('PARABÉNS!! você acertou!!')
elif n1 >=6:
    print('!!ERRO 404!! TENTE NOVAMENTE COM UM NÚMERO ENTRE 0 e 5')
else:
    print('O número é {}'.format(n2))
    print('Que pena! você errou!')


