#Calculadora de MULTA
print('=== DETRANZADA ===')
n1 = int(input('Qual foi a velocidade do veículo? KM/h '))
n2 = (n1 - 80) * 7
if n1 >= 81:
    print('MULTADO! O veículo ultrapassou a velocidade permitida que é de 80 km/h')
    print('Devendo pagar o valor de R$ {:.2f}'.format(n2))

print('Tenha um bom dia e dirija com segurança!')