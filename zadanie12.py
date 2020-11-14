rosliny_items=['storczyk', 'dracena']
rosliny_ilosc=[4, 1]
rosliny_ceny=[150, 120]

suma=0.0
for idx in range(len(rosliny_items)):
    item=rosliny_items[idx]
    ile=rosliny_ilosc[idx]
    cena=rosliny_ceny[idx] *ile
    print("{0} {1} {2}" .format(item, ile, cena))
    suma=suma+cena

if len(rosliny_items) > 3 and suma <= 500: #r1
    suma=suma-(suma*5)/100

elif len(rosliny_items) >3 and suma >= 500: #r2
    suma=suma-(suma*10)/100

elif len(rosliny_items) <3 and suma >= 500: #r2
    suma=suma-(suma*10)/100

print("Wartosc koszyka: {0}" .format(suma))
