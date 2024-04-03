compra = float(input("quanto custa sua compra? \nR$"))
cupom = float(input("quanto é seu desconto: "))

conta_porcentagem = (cupom * compra) / 100

desconto = compra - conta_porcentagem

print("Sua compra que custava {compra}," .format(compra=compra))
print("ganhou um desconto de 5%, passando a custar {desconto:.2f}" .format(desconto=desconto))