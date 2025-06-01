def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        return [list(map(int, line.strip().split())) for line in f]

def is_valid(levels):
    direction = None
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if direction is None:
            direction = diff > 0
        elif (diff > 0) != direction:
            return False

    return True

def is_valid_with_removal(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_valid(new_levels):
            return True
    return False

def partTwo():
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 2-input.txt")
    safe_count = 0
    for levels in data:
        if is_valid(levels) or is_valid_with_removal(levels):
            safe_count += 1
    print(safe_count)

def partOne():
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\day 2-input.txt")
    safe_count = 0
    for levels in data:
        if is_valid(levels):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    partOne()