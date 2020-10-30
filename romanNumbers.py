# Dictionnary with all possible roman numbers
numdict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
}

# save input of user as string
romNum = str(input("Römische nummer eingeben: "))

#translate the roman number to decimal
def translate(romNum):
    sum = 0
    prev_num = 0
    for char in romNum:                 # loop over every character in the roman number
        if numdict[char] > prev_num:    # if the found roman number is larger than the previous number, substract it (case: IX)
            sum -= prev_num             # subtract from total sum
        else:
            sum += prev_num             # else: add to the previous number (case: XI)
prev_num = numdict[char]                # update the previous number to the current number for the next iteration on the string
sum += prev_num                         # add the previous number to the total sum

    return sum

print("Dezimalzahl: " , translate(romNum))  # print out the result








