produkt={'ss12':{'nazwa': 'sukienka_trojka', 'rozmiary':['s', 'l', 'xl']},
'p12':{'nazwa': 'spodnie', 'rozmiary': ['s', 'xl']}}

for id in produkt:
    p =produkt[id]
    #print(id)
    print(p['nazwa'])
    r=p['rozmiary']
    for x in r:
        print(x)
