imie='Sylwia'
#ile=2
zwierze='ps'

print("Czesc, " +imie)
a=int(input("Podaj ilosc zwierzakow:"))
if a==1:
    print("{0} ma {1}a" .format(imie, zwierze))
elif a==2 or a==3:
    print('{0} ma {1} {2}y' .format(imie, a, zwierze))
else:
    print('{0} ma {1} {2}ow' .format(imie, a, zwierze))

"""print("{0} ma {1}eczka" .format(imie, zwierze))
print("{1} ma {0}eczka" .format(imie, zwierze))
print("{0} ma {1}eczka" .format(zwierze, imie))
print("{1} ma {0}eczka" .format(zwierze, imie))"""
