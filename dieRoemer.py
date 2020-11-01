roemische_zahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def getValueAt(text, index):
    # Check ob der Index innerhalb des Strings ist
    if index >= len(text):
        return 0
    
    # Check ob das Zeichen im Zeichenset ist
    if not text[index] in roemische_zahlen:
        return 0

    # Rückgabe des Wertes
    return roemische_zahlen[text[index]]


    # Erstellt eine Liste und fügt die dezimalen Werte der der römischen Zeichen an der jeweiligen Stelle ein
def romanTextToValues(text):
    werteliste = []
    for i in range(len(text)):
        werteliste.append(getValueAt(text, i))
    return werteliste
    
    # Findet die "negativen" Werte in der gegebenen Liste, damit ein "IX" auch korrekt erkannt wird.
def setNegativeValues(werteliste):
    for i in range(len(werteliste)-1):
        if werteliste[i] < werteliste[i + 1]:
            werteliste[i] = -werteliste[i]
    return werteliste

    # Berechnet den Wert der gegebenen römischen Zahl und wandelt sie in eine Dezimalzahl um.
def calculateRomanValue(text):
    werteliste = romanTextToValues(text)
    werteliste = setNegativeValues(werteliste)

    gesamtwert = 0
    for wert in werteliste:
        gesamtwert += wert
    
    return gesamtwert


while True:
    eingabe = input("Bitte eine römische Zahl eingeben: ").upper()
    wert = str(calculateRomanValue(eingabe))
    print("Der Wert von " + eingabe + " ist " + wert)