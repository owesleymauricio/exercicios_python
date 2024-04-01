texto = input('Digite algo: ')

print('o tipo primitivio é ', type(texto))
print('só tem espaço em branco? ', texto.isspace())
print('é um numero? ', texto.isnumeric())
print('é alfabetico? ', texto.isalpha())
print('é alfanumerico? ', texto.isalnum())
print('tem letra maiuscula? ', texto.isupper())
print('tem letra minuscula? ', texto.islower())
