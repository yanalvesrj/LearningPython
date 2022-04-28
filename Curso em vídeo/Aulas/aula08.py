import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('a raíz de {} é igual a {}'.format(num,math.ceil(raiz)))
#A outra maneira de importação é fazendo: from math import sqrt, por exemplo, que
#não precisa ficar referenciando toda a hora a biblioteca, como é o caso da linha 3.

#import emoji
print (emoji.emojize('Hello, World! :earth_americas:',use_aliases='true'))
