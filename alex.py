"""
S.83 (102/558) - N10.6

Schreiben Sie ein Python-Programm, das eine beliebige römische Zahl in eine
„gewöhnliche” Dezimalzahl umrechnet.
"""

#with help of Darkestry's code
dictionary_roemische_zahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

while True:
    print("Restart")
    input_in_letters = input("Input roman number ").upper()
    current_digit = 0
    previous_digit = 0
    
    for char in input_in_letters:
        if char in dictionary_roemische_zahlen:
            if dictionary_roemische_zahlen[char] > previous_digit:
                current_digit -= previous_digit
            else:
                current_digit += previous_digit
        previous_digit = dictionary_roemische_zahlen[char]
    current_digit += previous_digit

    print("Dezimalzahl: " + str(current_digit))