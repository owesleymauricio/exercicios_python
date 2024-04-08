celsius = float(input("Digite quantos °C está: "))

f = (celsius * 1.8) + 32

print('A temperatura de {celsius}°C corresponde a {f}°F.'
      .format(celsius=celsius, f=f)
      )