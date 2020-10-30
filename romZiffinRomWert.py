"""
#Python Programm zur Umrechnung von beliebligen römischen Zahlen in Dezimalzahlen
"""
#variablen

romZif = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

wert1 = 0
dezimal = 0

#input

romZahl = input("Bitte römische Zahl eingeben: ")

#methoden

#für jeden character aus der Eingabe wird folgendes durchgeführt
for char in romZahl:
    #wenn der character in dem Dictionary vorhanden ist
    if char in romZif:
        #soll er mit dem vorherigen wert1 verglichen werden
        
            #falls er größer ist als wert1, wird der wert1 von dezimal subtrahiert
        if romZif[char] > wert1:
            dezimal -= wert1
            #ansonsten wird dezimal und wert addiert
            
        else:
            dezimal += wert1
            
    # wert 1 soll romZif aus dem eingegebenen input werden       
    wert1 = romZif[char]
#dezimal plus wert1 sei dezimal
dezimal += wert1
    
#das ergebnis ist ein String aus dezimal
print("Ergebnis: " + str(dezimal))


