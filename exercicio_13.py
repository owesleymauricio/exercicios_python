salario = float(input("Qual o seu salario mensal? \nR$"))
aumento_de_salario = float(input("quanto % voce ganhou de aumento: "))

conta_porcentagem = (aumento_de_salario * salario) / 100

salario_com_aumento = salario + conta_porcentagem

print("Seu salario era R${salario} Reais." .format(salario=salario))
print("com o aumento de {aumento}%, passou a ser R${novo_salario:.2f} Reais" .format(novo_salario=salario_com_aumento, aumento=aumento_de_salario))