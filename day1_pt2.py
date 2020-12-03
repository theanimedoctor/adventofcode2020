def read_int(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def findSumLocations(intList):
    length = len(intList)
    for x in range(length):
        for y in range(length):
            for z in range(length):
                if (x != y) and (y != z) and (x != z):
                    if expenses[x] + expenses[y] + expenses[z] == 2020:
                        print(expenses[x], " ", expenses[y], " ", expenses[z])
                        return expenses[x] * expenses[y] * expenses[z]

expenses = read_int("input.txt")
print(findSumLocations(expenses))
