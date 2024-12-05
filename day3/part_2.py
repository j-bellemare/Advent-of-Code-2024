import re

input_file = open("corrupted_memory.txt", "r")
pattern = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"
mul_pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"

data = input_file.read()
matches = re.findall(pattern, data)

total = 0
on = True

for match in matches:
    if match == "don't()":
        on = False
    if match == "do()":
        on = True
    elif on is True:
        mult = re.findall(mul_pattern, match)

        total += int(mult[0][0]) * int(mult[0][1])

print(total)
