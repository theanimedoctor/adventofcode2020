def readStr(filename):
    with open(filename) as f:
        return [str(x) for x in f]


def position(right, down, path):
    horizontalPos = 0
    patternWidth = len(path[0]) - 1
    treesHit = 0
    for verticalPos in range(0, len(path), down):
        if path[verticalPos][horizontalPos] == "#":
            treesHit += 1
        if horizontalPos + right >= patternWidth:
            horizontalPos = right - patternWidth + horizontalPos
        else:
            horizontalPos += right
        
    return treesHit




path = readStr("inputDay3.txt")
#print(path)
print(position(1, 1, path))
print(position(3, 1, path))
print(position(5, 1, path))
print(position(7, 1, path))
print(position(1, 2, path))