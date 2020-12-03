
def readPassPolicy(string):
    minimum = ""
    maximum = ""
    letter = ""
    password = ""
    curChar = 0
    while string[curChar] != "-":
        minimum += string[curChar]
        curChar += 1
    curChar += 1
    while string[curChar] != " ":
        maximum += string[curChar]
        curChar += 1
    letter = string[curChar + 1]
    curChar += 4
    while string[curChar] != "\n":
        password += string[curChar]
        curChar += 1
    policy = [int(minimum), int(maximum), letter, password]
    return policy

def readStr(filename):
    with open(filename) as f:
        return [str(x) for x in f]
    

def countChar(character, string):
    count = 0
    for element in string:
        if element == character:
            count += 1
    return count

def checkValidPass(passAndPolicyList):
    count = 0
    for x in range(len(passAndPolicyList)):
        currPolicy = readPassPolicy(passAndPolicyList[x])
        policyCharInPass = countChar(currPolicy[2], currPolicy[3])
        if policyCharInPass >= currPolicy[0] and policyCharInPass <= currPolicy[1]:
            count += 1
    return count

inputs = readStr("inputDay2.txt")
print(checkValidPass(inputs))