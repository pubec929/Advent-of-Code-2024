def print_map(map_):
    for row in map_:
        print(row)

def locate(map_, target):
    for i, row in enumerate(map_):
        if target in row:
            return [i, row.index(target)]
    raise ValueError

def get(map_, coords):
    return map_[coords[0]][coords[1]]

def turn(direction):
    directions = ["up", "right", "down", "left"]
    avatars = ["^", ">", "v", "<"]
    i = (directions.index(direction) + 1) % 4
    return directions[i], avatars[i]

def on_board(coords, length, height):
    return 0 < coords[0] < height - 1 and 0 < coords[1] < length - 1 

def part_one():
    map_ = open(r"D:\Paul\Coding Stuff\Python\Advent of Code 2024\data\day 6-input.txt", "r", encoding="utf-8").readlines()
    map_ = list(map(lambda r: list(r.strip()), map_))
    length = len(map_[0])
    height = len(map_)
    avatar = "^"
    coords = locate(map_, avatar)
    direction = "up"
    while on_board(coords, length, height):
        new_coords = []
        print(length, height, coords)
        if direction == "up":
            new_coords = [coords[0]-1, coords[1]]
        elif direction == "left":
            new_coords = [coords[0], coords[1]-1] 
        elif direction == "right":
            new_coords = [coords[0], coords[1]+1] 
        elif direction == "down":
            new_coords = [coords[0]+1, coords[1]]
        if get(map_, new_coords) != "#":
            map_[coords[0]][coords[1]] = "X"
            map_[new_coords[0]][new_coords[1]] = avatar
            coords = new_coords
        else:
            direction, avatar = turn(direction)
    total = 1
    for row in map_:
        total += row.count("X")
    print(total)


if __name__ == "__main__":
    part_one()