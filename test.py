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
        if r not in rules.keys():
            rules[r] = []
    for key in sorted(rules.keys()):
        print(f"Key {key}: {sorted(rules[key])}")


if __name__ == "__main__":
    main()