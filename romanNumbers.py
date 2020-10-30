numdict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
}

romNum = str
romNum = str(input("Römische nummer eingeben: "))

def translate(romNum):
    sum = 0
    prev_num = 0
    for char in romNum:
        if char in numdict:
            if numdict[char] > prev_num:
                sum -= prev_num
            else:
                sum += prev_num
        prev_num = numdict[char]
    sum += prev_num

    return sum

print("Dezimalzahl: " , translate(romNum))








