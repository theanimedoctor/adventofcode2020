
def readPassPolicy(string):
    firstPosition = ""
    secondPosition = ""
    letter = ""
    password = ""
    curChar = 0
    while string[curChar] != "-":
        firstPosition +=  string[curChar]
        curChar += 1
    curChar += 1
    while string[curChar] != " ":
        secondPosition += string[curChar]
        curChar += 1
    letter = string[curChar + 1]
    curChar += 4
    while string[curChar] != "\n":
        password += string[curChar]
        curChar += 1
    policy = [int(firstPosition), int(secondPosition), letter, password]
    return policy

def readStr(filename):
    with open(filename) as f:
        return [str(x) for x in f]
    

def checkValidPass2(passAndPolicyList):
    count = 0
    for x in range(len(passAndPolicyList)):
        currPolicy = readPassPolicy(passAndPolicyList[x])
        first = (currPolicy[2] == currPolicy[3][currPolicy[0] - 1])
        second = (currPolicy[2] == currPolicy[3][currPolicy[1] - 1])
        if (first and not second) or (second and not first):
            count += 1
    return count

inputs = readStr("inputDay2.txt")
print(checkValidPass2(inputs))