'''
Aufgabe: Schreiben Sie ein Python-Programm, das eine beliebige römische Zahl in eine
         „gewöhnliche” Dezimalzahl umrechnet.
'''

roemische_zahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #Erstelle ein Dictionary
dezimal_zahlen = 0

if __name__ == "__main__":
    input_roemisch = input("Römische Zahl eingeben: ")

vorherige_zahl = 0
for char in input_roemisch:
    if char in roemische_zahlen:
        if roemische_zahlen[char] > vorherige_zahl:
            dezimal_zahlen -= vorherige_zahl
        else:
            dezimal_zahlen += vorherige_zahl
    vorherige_zahl = roemische_zahlen[char]
dezimal_zahlen += vorherige_zahl

print("Als Dezimalzahl: " + str(dezimal_zahlen))
