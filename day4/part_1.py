import re

input_file = open("word_search.txt", "r")
pattern = r"XMAS"
pattern2 = r"SAMX"
total = 0

data1 = []
for line in input_file:
    data1.append(line.strip())

data2 = []
for line in data1:
    i = 0
    for char in line:
        if i not in range(len(data2)):
            data2.append('')
        data2[i] = str(data2[i]) + char
        i += 1


rows = len(data1)
cols = max(len(line) for line in data1)
data3 = []
data4 = []
for line in data1:
    data4.append("".join(reversed(line)))


def collect_diagonal(r, c, data):
    diagonal = []
    while 0 <= r < rows and 0 <= c < cols:
        diagonal.append(data[r][c])
        r += 1  # Move down
        c += 1  # Move right
    return ''.join(diagonal)


for col in range(cols):
    data3.append(collect_diagonal(0, col, data1))

for row in range(1, rows):
    data3.append(collect_diagonal(row, 0, data1))

for col in range(cols):
    data3.append(collect_diagonal(0, col, data4))

for row in range(1, rows):
    data3.append(collect_diagonal(row, 0, data4))


def find_all(data):
    matches = []
    for line in data:
        matches += re.findall(pattern, line)
        matches += re.findall(pattern, "".join(reversed(line)))
    return len(matches)


total = find_all(data1) + find_all(data2) + find_all(data3)

print(total)
