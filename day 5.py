

def main():
    data = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 5-input.txt", "r", encoding="utf-8").readlines()
    rules = {}
    for i, row in enumerate(data):
        if row.strip() == "":
            break
        l, r = row.strip().split("|")
        if l in rules:
            rules[l].append(r)
        else:
            rules[l] = [r]
        # if r not in rules.keys():
        #     print(r)
        #     rules[r] = []
    total = 0
    # print(rules["99"])
    # for x in sorted(rules.keys()):
    #     print(x, sorted(rules[x]))
    for row in data[i+1:]:
        row = row.strip().split(",")
        
        middle = 0
        safe = True
        for index, num in enumerate(row[:len(row)-1]):
            if index == len(row) // 2:
                middle = num
            if row[index + 1] not in rules[num]:
                safe = False
                break
        print(row, safe)
        if safe:
            #print(row, safe)
            total += int(middle)
    print(total)


if __name__ == "__main__":
    main()