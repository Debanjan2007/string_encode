salt = "A9fQm2Xb" #random 8 bit text generated
bad_codes = list(range(0, 32)) + [127]

# encode programe
def encode(str) : 
    str.strip() 
    Strlist = list()
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
        if i in bad_codes:
            i += 1  # Skip to next valid code
        finalAsciiVals.append(i)
    # converting to final char val
    for i in finalAsciiVals:
        newStr = chr(i) 
        Strlist.append(newStr)
    Strlist.reverse() # reverse for better encode
    finalStr = salt.join(Strlist)
    return finalStr 

# decode programe
def decode(str) :
    strSplitLIst = [x for x in str.split(salt) if x]  # removes empty elements
    asciiVals = [] 
    finalStrList = []
    strSplitLIst.reverse()
    for newElm in strSplitLIst:
        ascival = ord(newElm)
        asciiVals.append(ascival)
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