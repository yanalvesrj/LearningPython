#MANEIRA MATEMÁTICA DE RESOLVER
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hp = (co ** 2 + ca **2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hp))

#MANEIRA IMPORT (.hypot) DE RESOLVER
from math import hypot
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hp = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hp))