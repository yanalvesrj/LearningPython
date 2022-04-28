dias = int(input('Quantos dias o veículo foi alugado? '))
kms = float(input('Quantos KMs rodados? '))
da= dias*60
#da = dias alugados
kmr= kms * 0.15
#kmr = KMs rodados
val= kmr + da
print('O veículo foi alugado por {} dias e rodou {:.2f}KMs'.format(dias,kms))
print('O valor a pagar é de R${:.2f}'.format(val))
#Dá pra fazer juntando os dois valores da e kmr na mesma variável!
#Exemplo: val = (dias*60) + (kms*0.15)
