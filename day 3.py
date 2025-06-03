import re

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def partOne():
    data = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 3-input.txt", "r", encoding="utf-8").read()
    matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data)
    total = sum(int(a) * int(b) for a, b in matches)
    print(total)
def partTwo():
    result = 0
    numbers = "0123456789"
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 3-input.txt")
    start_sequence = False
    l = ""
    r = ""
    direction = "l"
    i = 0
    isEnabled = True
    while i < len(data):   
        if start_sequence:
            if data[i] == "," and l != "" and r == "":
                direction = "r"
            elif data[i] == ")" and l != "" and r != "":
                print(l, r, result)
                result += int(l) * int(r)
                l = ""
                r = ""
                direction = "l"
                start_sequence = False
            elif data[i] not in numbers:
                l = ""
                r = ""
                direction = "l"
                start_sequence = False
            else:
                if direction == "l":
                    l += data[i]
                else: 
                    r += data[i]
                if len(l) >= 4 or len(r) >= 4:
                    l = ""
                    r = ""
                    direction = "l"
                    start_sequence = False

                
        if data[i:i+4] == "mul(" and isEnabled:
            print("found start sequence")
            start_sequence = True
            i += 4
            continue
        elif data[i:i+7] == "don't()":
            isEnabled = False
        elif data[i:i+4] == "do()":
            isEnabled = True
        i += 1
    print(result)

if __name__ == "__main__":
    partOne()