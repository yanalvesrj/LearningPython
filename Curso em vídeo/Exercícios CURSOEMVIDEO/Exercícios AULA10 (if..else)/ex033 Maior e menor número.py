v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

maior = v1  # Saber o maior número
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
menor = v1  # Saber o menor número
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
    
print('O maior valor digitado foi {}'.format(maior))
print('E o menor valor digitado foi {}'.format(menor))
