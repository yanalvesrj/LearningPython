# Verificador de nomes, primeiro e ultimo nome
nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Muito prazer, {}'.format(n[0]))
print('Seu primeiro nome é {}'.format(n[0]))
print('E seu ultimo nome é {}'.format(n[len(n) - 1]))
