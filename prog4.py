kolory=['zolty', 'czarny', 'pomaranczowy', 'zielony', 'bialy']

print("opcja1")
print(kolory[2])
print(kolory[4])

print("opcja 2")
for k in kolory:
    print(k)

print("opcja3")
for k in range(len(kolory)):
    print("k: " +str(k) +": " +kolory[k])

print("tej nie rozumiem")
print("len: {0}".format(len(kolory)))
print("range: {0}".format(range(5)))
print(range(5))
