carro_alugado = int(input('Por qunatos dias você alugou o carro?: '))

km_rodados = float(input('Quantos KM você rodou?: '))

resultado = (carro_alugado * 60) + (km_rodados * 0.15)

print('voce ira pagar {resultado:.2f}' .format(resultado=resultado))