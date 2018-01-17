# -*- coding: utf-8 -*-

kvocient = 0.621371

print "Pozdravljeni v pretvorniku enot iz kilometrov v milje ter obratno."

while True:
    print "Prosimo, izberite način:\n 1. pretvorba kilometrov v milje\n 2. pretvorba milj v kilometre\n 3. Izhod"

    try:
        vnos_nacina = int(raw_input())
    except Exception as e:
        print "Vpišite številko!"
        continue

    if vnos_nacina == 1:
        while True:
            print "Vpišite število kilometrov, ki jih želite pretvoriti v milje. Z 'x' greste na začetek!"
            vnos = raw_input()
            try:
                rezultat = float (vnos) * kvocient
            except Exception as e:
                if vnos == 'x':
                    break
                print "Vpišite številko!"
                continue
            print rezultat
            print "Ali želite nadaljevati s pretvarjanjem? (da/ne)"
            dodatno = raw_input()
            if dodatno != 'da':
                exit(0)

    if vnos_nacina == 2:
        while True:
            print "Vpišite število milj, ki jih želite pretvoriti v kilometre. Z 'x' greste na začetek!"
            vnos = raw_input()
            try:
                rezultat = float(vnos) / kvocient
            except Exception as e:
                if vnos == 'x':
                    break
                print "Vpišite številko!"
                continue
            print rezultat
            print "Ali želite nadaljevati s pretvarjanjem? (da/ne)"
            dodatno = raw_input()
            if dodatno != 'da':
                exit(0)


    if vnos_nacina == 3:
        exit(0)

    else:
       print "Veljavni izbiri sta 1. in 2."