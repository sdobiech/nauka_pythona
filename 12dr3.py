rosliny_items=['storczyk', 'dracena', 'aloes', 'fikus']
rosliny_ilosc=[1, 1, 6, 1]
rosliny_ceny=[150, 120, 30, 100]
ceny_do_obliczen=[]
#print(min(rosliny_ceny))
suma=0.0
for idx in range(len(rosliny_items)):
    item=rosliny_items[idx]
    ile=rosliny_ilosc[idx]
    cena=rosliny_ceny[idx] *ile
    ceny_do_obliczen.append(cena)
    #print(ceny_do_obliczen)
    #print(min(ceny_do_obliczen))
    print("{0} ilosc: {1} cena za sztuke: {2} lacznie: {3}" .format(item, ile, rosliny_ceny[idx], cena))
    suma=suma+cena

suma1=suma-min(ceny_do_obliczen)

print("Wartosc koszyka: {0}" .format(suma1))
