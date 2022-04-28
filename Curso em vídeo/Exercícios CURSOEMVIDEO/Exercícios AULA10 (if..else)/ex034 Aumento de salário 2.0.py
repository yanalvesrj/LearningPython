salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:  # Aumento a partir de R$1250
    n1 = (salario * 10 / 100) + salario
    print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salario, n1))
elif salario <= 1250:  # Aumento a baixo de R$1250
    n2 = (salario * 15 / 100) + salario
    print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salario, n2))
