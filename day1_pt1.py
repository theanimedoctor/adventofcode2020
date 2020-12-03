def read_int(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def findSumLocations(intList):
    length = len(intList)
    for x in range(length):
        for y in range(length):
            if (x != y):
                if expenses[x] + expenses[y] == 2020:

                    return expenses[x] * expenses[y]

expenses = read_int("input.txt")
print(findSumLocations(expenses))
