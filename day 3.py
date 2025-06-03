def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def main():
    result = 0
    numbers = "0123456789"
    data = readFile("D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 3-input.txt")
    start_sequence = False
    l = ""
    r = ""
    direction = "l"
    i = 0
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

                
        if data[i:i+4] == "mul(":
            print("found start sequence")
            start_sequence = True
            i += 4
            continue
        
        i += 1
    print(result)
    


if __name__ == "__main__":
    main()