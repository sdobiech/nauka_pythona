worki_do_zywienia={'name': 'Smofkabiven',
        'marka': 'Fresenius',
        'objetosc': 986,
        'komory': 3}

for key in worki_do_zywienia:
        print("{0}: {1}".format(key, worki_do_zywienia[key]))

for key, value in worki_do_zywienia.items():
        print("{0}:{1}".format(key, value))
