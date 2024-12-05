import re

input_file = open("./inputs/corrupted_memory.txt", "r")
pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"

data = input_file.read()
matches = re.findall(pattern, data)

total = 0
for pair in matches:
    total += int(pair[0]) * int(pair[1])

print(total)
