def readStr(filename):
    with open(filename) as f:
        return [str(x) for x in f]


def position(path):
    horizontalPos = 0
    patternWidth = len(path[0]) - 1
    treesHit = 0
    for verticalPos in range(len(path)):
        if path[verticalPos][horizontalPos] == "#":
            treesHit += 1
        if horizontalPos + 3 >= patternWidth:
            horizontalPos = 3 - patternWidth + horizontalPos
        else:
            horizontalPos += 3
        
    return treesHit




path = readStr("inputDay3.txt")
print(position(path))