
#Identificador de Unidades numéricas 0 a 9999

n = int(input('Digite um número: '))
u = n //1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))