# def check(rules, updates):
#     #print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n\n")
#     for row in updates:
#         safe = True
#         for index, num in enumerate(row[:len(row)-1]):
#             if index == len(row) // 2:
#                 middle = num
#             if row[index + 1] not in rules[num]:
#                 safe = False
#                 break
        
#         #print(row, safe)

def main():
    data = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 5-input.txt", "r", encoding="utf-8").readlines()
    global rules
    rules = {}
    for i, row in enumerate(data):
        if row.strip() == "":
            break
        l, r = row.strip().split("|")
        if l in rules:
            rules[l].append(r)
        else:
            rules[l] = [r]
        if r not in rules.keys():
            rules[r] = []
    total = 0
    # print(rules["99"])
    # for x in sorted(rules.keys()):
    #     print(x, sorted(rules[x]))
    #new_data = []
    for row in data[i+1:]:
        row = row.strip().split(",")
        #print(row == ["68", "11", "75", "89", "42", "49", "62", "86", "24"])
        safe = True
        #print(row)
        for index in range(len(row) - 1):
            num = row[index]
            if row[index + 1] not in rules[num]:
                curr = index
                safe = False
                row = sort(row)
        #print(row, safe)
        #new_data.append(row)
        if not safe:
            total += int(row[len(row)//2])
    #check(rules, new_data[-5:])
    print(total)

def sort(array):
    sorted_array = [array[0]]
    for num in array[1:]:
        for i, comp in enumerate(sorted_array):
            if comp in rules[num]:
                sorted_array.insert(i, num)
                break
            if i == len(sorted_array) - 1:
                sorted_array.append(num)
                break
    return sorted_array
    


if __name__ == "__main__":
    main()
    output = sort(['68', '11', '75', '89', '42', '49', '62', '86', '24'])
    #check(rules, [output])