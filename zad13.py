koszyk={'chleb':6, 'ser':10, 'mleko':3, 'jajka':8}

#for key in koszyk:
#    print("{0}:{1}".format(key, koszyk[key]))

suma=0.0
for key in koszyk:
        cena=koszyk[key]
        print("{0}: {1}".format(key, koszyk[key]))
        suma=suma+cena

print(suma)

if 'ser' in koszyk and 'mleko' in koszyk:
    print("Kwota przed obnizka: ", suma)
    print('Znizka')
    suma=suma-(suma*10)/100
    print("Wartosc po obnizce: " +str(suma))
