
def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        contents = f.readlines()

    start = []
    end = []
    for row in contents:
        l, r = row.strip().split()
        start.append(int(l))
        end.append(int(r))

    return start, end


def partOne():
    start, end = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 1-input.txt")
    start.sort()
    end.sort()
    
    distance = 0
    for i in range(0, len(end)):
        distance += abs(start[i] - end[i])
    print(distance)

def partTwo():
    left, right = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 1-input.txt")
    count = {}
    similarityScore = 0
    for num in right:
        if num in count:
            count[num] += 1
        else: 
            count[num] = 1
    
    for num in left:
        if num in count:
            similarityScore += count[num] * num
    print(similarityScore)
    

if __name__ == "__main__":
    partOne()
    partTwo()