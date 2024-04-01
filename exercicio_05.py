numero = int(input('digite um numero: '))

antecessor = numero - 1
sucessor = numero + 1

print('o antecessor de {numero} é {antecessor}, e o sucessor é {sucessor}'
      .format(numero=numero, antecessor=antecessor, sucessor=sucessor)
      )