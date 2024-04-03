real = float(input('quantos Reais voce tem? \n R$'))
dollar = float(input('qual a cotaçao do dollar? \n R$'))

cotacao = real / dollar

print("convertido você tem ${cotacao:.2f} dollar(s)"
      .format(cotacao=cotacao)
      )
