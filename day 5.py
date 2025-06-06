def split_data(data):
    for i, row in enumerate(data):
        if row.strip() == "":
            break
    return data[:i], data[i+1:]


def format_rules(rules):
    formated_rules = {}
    for row in rules:
        l, r = list(map(lambda n: int(n), row.strip().split("|")))
        if l in formated_rules:
            formated_rules[l].append(r)
        else:
            formated_rules[l] = [r]
        if r not in formated_rules.keys():
            formated_rules[r] = []
    return formated_rules

def part_one():
    data = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 5-input.txt", "r", encoding="utf-8").readlines()
    rules, updates = split_data(data)
    rules = format_rules(rules)
    total = 0
    for row in updates:
        row = list(map(lambda n: int(n), row.strip().split(",")))
        safe = True
        for index, num in enumerate(row[:len(row)-1]):
            if row[index + 1] not in rules[num]:
                safe = False
                break
        if safe:
            total += row[len(row)//2]
    print(total)

def part_two():
    data = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 5-input.txt", "r", encoding="utf-8").readlines()
    rules, updates = split_data(data)
    rules = format_rules(rules)
    total = 0
    for row in updates:
        row = list(map(lambda n: int(n), row.strip().split(",")))
        sorted_row = sort(rules, row)
        if sorted_row != row:
            total += int(sorted_row[len(sorted_row)//2])
    print(total)
    

def sort(rules, array):
    sorted_array = [array[0]]
    for num in array[1:]:
        for i, comp in enumerate(sorted_array):
            if comp in rules[num]:
                sorted_array.insert(i, num)
                break
        if i == len(sorted_array) - 1:
            sorted_array.append(num)
    return sorted_array
    


if __name__ == "__main__":
    part_one()
    #check(rules, [output])