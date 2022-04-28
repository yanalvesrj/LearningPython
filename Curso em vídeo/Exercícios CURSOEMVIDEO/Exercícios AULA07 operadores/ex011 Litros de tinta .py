lar = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
are = lar * alt
tin = are / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar,alt,are))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tin))
