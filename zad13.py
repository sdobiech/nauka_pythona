dodatki={'supliven':10, 'soluvit':10, 'vitalipid':10}

#for key in koszyk:
#    print("{0}:{1}".format(key, koszyk[key]))

objetosc=0.0
for key in dodatki:
        vol=dodatki[key]
        print("{0}: {1}".format(key, dodatki[key]))
        objetosc=objetosc+vol

print(objetosc)

if 'soluvit' in dodatki and 'supliven' in dodatki:
    print("Objetosc przed korekta: ", objetosc)
    objetosc=objetosc-10
    print("Objetosc po korekcie: " +str(objetosc))
