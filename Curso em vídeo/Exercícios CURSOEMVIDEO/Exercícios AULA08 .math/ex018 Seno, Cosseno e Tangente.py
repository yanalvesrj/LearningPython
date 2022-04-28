#SENO COSSENO E TANGENTE
import math
an = float(input('Digite o angulo que você deseja: '))
sen = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tangente))


