roemischeZahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


while True:
    rZ = input("Bitte eine römische Zahl eingeben: ")
    wert = 0

    for i in range(len(rZ) - 1):
        if roemischeZahlen[rZ[i]] < roemischeZahlen[rZ[i+1]]:
            wert -= roemischeZahlen[rZ[i]]
        else: 
            wert += roemischeZahlen[rZ[i]]
    wert += roemischeZahlen[rZ[-1]]

    print(wert)