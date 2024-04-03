medida = float(input('digite a distancia em metros: '))

km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(
    'em Km: {km}\nem hm: {hm}\nem dam: {dam}\nem metro(s): {m}\nem dm: {dm}\nem cm: {cm}\nem mm: {mm}'
    .format(km=km, 
            hm=hm,
            dam=dam,
            m=m,
            dm=dm,
            cm=cm,
            mm=mm
            )
    )