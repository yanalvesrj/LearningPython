#Condicionais If...Else
n1 = float(input('Digite sua primeira nota? '))
n2 = float(input('Digite sua segunda nota? '))
m = (n1+n2)/2
if m <= 6.0:
    print('Média de {:.1f}! Aluno REPROVADO!!'.format(m))
else:
    print('Média de {:.1f}! Aluno APROVADO!'.format(m))
