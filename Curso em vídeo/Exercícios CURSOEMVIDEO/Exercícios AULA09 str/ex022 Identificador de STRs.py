
#Identificador de STRs

frase = str(input('Digite seu nome: ')).strip()
print ('Analisando seu nome...')
print ('Seu nome em letras maiúsculas é {}'.format(frase.upper()))
print ('Seu nome em letras minúsculas é {}'.format(frase.lower()))
print ('Seu nome ao todo tem {} letras'.format(len(frase) - frase.count(' ')))
print ('E a quantidade de letras no primeiro nome é {}'.format(frase.find(' ')))
