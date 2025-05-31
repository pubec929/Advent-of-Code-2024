def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        contents = f.readlines()

    matrix = []
    for row in contents:
        matrix.append(list(map(int, row.strip().split())))
    
    return matrix
    
def check(l, r, isIncreasing):
    ...


def partOne():
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 2-input.txt")
    safeCounter = 0
    for level in data:
        isIncreasing = None
        isSafe = True
        for i in range(len(level) - 1):
            difference = level[i] - level[i + 1]
            if isIncreasing == None:
                isIncreasing = difference < 0 
            else:
                if isIncreasing != (difference < 0):
                    isSafe = False
                    break

            if abs(difference) == 0 or abs(difference) >= 4:
                isSafe = False
                break 

        if isSafe:
            safeCounter += 1
    print(safeCounter)
def partTwo():
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 2-input.txt")
    safeCounter = 0
    for level in data:
        isIncreasing = None
        isSafe = True
        for i in range(len(level) - 1):
            difference = level[i] - level[i + 1]
            if isIncreasing == None:
                isIncreasing = difference < 0 
            else:
                if isIncreasing != (difference < 0):
                    isSafe = False
                    check(level[i-1], level[i+1], isIncreasing)
                    break

            if abs(difference) == 0 or abs(difference) >= 4:
                isSafe = False
                break 

        if isSafe:
            safeCounter += 1
    print(safeCounter)

if __name__ == "__main__":
    partTwo()