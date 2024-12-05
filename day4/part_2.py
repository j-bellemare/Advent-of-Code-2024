input_file = open("word_search.txt", "r")

data = []
for line in input_file:
    data.append(line.strip())

count = 0
row = 0
for line in data:
    col = 0
    for char in line:
        if (
            char == "A"
            and (row > 0 and col > 0)
            and (row < len(data) - 1 and col < len(line) - 1)
        ):
            if (data[row - 1][col - 1] == "M" and data[row + 1][col + 1] == "S") or (
                data[row - 1][col - 1] == "S" and data[row + 1][col + 1] == "M"
            ):
                if (
                    data[row - 1][col + 1] == "M" and data[row + 1][col - 1] == "S"
                ) or (data[row - 1][col + 1] == "S" and data[row + 1][col - 1] == "M"):
                    count += 1
        col += 1
    row += 1

print(count)
