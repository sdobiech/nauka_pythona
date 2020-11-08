rosliny_items=['storczyk', 'dracena', 'fikus', 'aloes']
rosliny_ilosc=[1, 2, 1, 3]
rosliny_ceny=[300, 200, 100, 50]

suma=0.0
for idx in range(len(rosliny_items)):
    item=rosliny_items[idx]
    ile=rosliny_ilosc[idx]
    cena=rosliny_ceny[idx] *ile
    print("{0} {1} {2}" .format(item, ile, cena))
    suma=suma+cena

'''if 'storczyk' in rosliny_items and 'dracena' in rosliny_items: #r2
    print("Kwota przed obnizka: ", suma)
    print('Znizka')
    suma=suma-(suma*10)/100'''

if len(rosliny_items) > 3: #r1
    suma=suma-(suma*5)/100

if suma >= 500: #r2
    print("Znizka R2:")
    suma=suma-(suma*10)/100


print("Wartosc koszyka: {0}" .format(suma))
