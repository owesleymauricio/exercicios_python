largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

metros_quadrado = largura * altura
quantidade_tinta = (metros_quadrado / 2)

print('sua parede tem a dimensão de {largura}x{altura}, sua area é de {metros_quadrado:.3}m²'
      .format(largura=largura, altura=altura, metros_quadrado=metros_quadrado)
      )

print('Para pintar a parede você precisa de{quantidade_tinta:.3}l de tinta'
      .format(quantidade_tinta=quantidade_tinta)
      )