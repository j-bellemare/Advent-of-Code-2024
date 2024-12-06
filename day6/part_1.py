import time

input_file = open("./inputs/test.txt", "r")

floor_map = []
i = 0
for line in input_file:
    for char in line.strip():
        if i not in range(len(floor_map)):
            floor_map.append([])
        floor_map[i].append(char)
    i += 1

patrol = True
loops = 0
row1 = 0
for line1 in floor_map:
    col1 = 0
    for char1 in line1:
        if char1 == ".":
            floor_map[row1][col1] = "#"

        timeout = 60
        timeout_start = time.time()
        not_timed_out = True

        while patrol is True and not_timed_out is True:
            if time.time() > timeout_start + timeout:
                not_timed_out = False
                loops += 1
            row = 0
            for line in floor_map:
                col = 0
                for char in line:
                    if (
                        (char == "^" and row == 0)
                        or (char == "v" and row == len(floor_map) - 1)
                        or (char == "<" and col == 0)
                        or (char == ">" and col == len(line) - 1)
                    ):
                        patrol = False

                    if char == "^" and row > 0:
                        if floor_map[row - 1][col] != "#":
                            floor_map[row - 1][col] = "^"
                        elif col + 1 > len(line) - 1:
                            patrol = False
                        elif floor_map[row][col + 1] != "#":
                            floor_map[row][col + 1] = ">"
                        else:
                            floor_map[row - 1][col] = "v"

                    elif char == "v" and row < len(floor_map) - 1:
                        if floor_map[row + 1][col] != "#":
                            floor_map[row + 1][col] = "v"
                        elif col - 1 < 0:
                            patrol = False
                        elif floor_map[row][col - 1] != "#":
                            floor_map[row][col - 1] = "<"
                        else:
                            floor_map[row + 1][col] = "^"

                    elif char == "<" and col > 0:
                        if floor_map[row][col - 1] != "#":
                            floor_map[row][col - 1] = "<"
                        elif row - 1 < 0:
                            patrol = False
                        elif floor_map[row - 1][col] != "#":
                            floor_map[row - 1][col] = "^"
                        else:
                            floor_map[row][col + 1] = ">"

                    elif char == ">" and col < len(line) - 1:
                        if floor_map[row][col + 1] != "#":
                            floor_map[row][col + 1] = ">"
                        elif row + 1 > len(floor_map) - 1:
                            patrol = False
                        elif floor_map[row + 1][col] != "#":
                            floor_map[row + 1][col] = "v"
                        else:
                            floor_map[row][col - 1] = "<"

                    if char in ["^", "v", ">", "<"]:
                        floor_map[row][col] = "X"

                    col += 1
                row += 1
            if char1 == ".":
                floor_map[row1][col1] = "."
        col1 += 1
    row1 += 1

for line in floor_map:
    print(line)

total = 0
for line in floor_map:
    for char in line:
        if char == "X":
            total += 1

print(loops)
