print('listy na string')
kolory=['zolty', 'czarny', 'pomaranczowy', 'zielony', 'bialy']
print(kolory)
print(",".join(kolory))

print('string na listy')
import_kolory='zolty;czarny;pomaranczowy;zielony;bialy'
print(import_kolory)
lista=import_kolory.split(',')
print(lista)
