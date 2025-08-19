salt = "A9fQm2Xb" #random 8 bit text generated

# encode programe
def encode(str) : 
    str.strip() 
    Hexlist = list()
    asciiVals = list()
    finalAsciiVals = list()
    strSplitList = str.split() 
    # converting into ascii values
    for elm in strSplitList:
        for i in elm : # here i denotes every index
            asciiVal = ord(i)
            asciiVals.append(asciiVal)
    #increasing the ascii values
    for i in asciiVals:
        i = i + 2 * asciiVals.index(i)
        finalAsciiVals.append(i)
    # converting to final char val
    for i in finalAsciiVals:
        Hexlist.append(hex(i))
    Hexlist.reverse()
    Str = salt.join(Hexlist)
    return Str
# decode programe
def decode(str) :
    strSplitLIst = str.split(salt) # removes empty elements
    asciiVals = [] 
    finalStrList = []
    strSplitLIst.reverse()
    for newElm in strSplitLIst:
        intval = int(newElm , 16)
        asciiVals.append(intval)
    for i in asciiVals:
        i = i - 2 * asciiVals.index(i)
        strPart = chr(i)
        finalStrList.append(strPart)
    finalStr = "".join(finalStrList)
    return finalStr

print("Enter <1> for encode \n Enter <2> for decode")
choice = input("Enter your choice : ")
if choice == '1' :
    str = input("Enter your string here :")
    encoded = encode(str)
    print(encoded)
elif choice == '2' :
    str = input("Enter your encoded string here :")
    decoded = decode(str)
    print(decoded)
else : 
    print("Please enter a right choice !!")