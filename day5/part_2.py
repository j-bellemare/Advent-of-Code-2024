import re

input_file = open("./inputs/page_r_p.txt", "r")

pattern = r"\b\d{2}\b"

switch = False
rules = []
prints = []
for line in input_file:
    if line.strip():
        if switch is False:
            rules.append(line.strip())
        if switch is True:
            prints.append(line.strip())
    else:
        switch = True

full_prints = []
for line in prints:
    nums = re.findall(pattern, line)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    full_prints.append(nums)

full_rules = []
for line in rules:
    nums = re.findall(pattern, line)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    full_rules.append(nums)

good_lines = []
for line in full_prints:
    good_line = True
    for num in line:
        for rule in full_rules:
            if num == rule[0]:
                if rule[1] in line:
                    if line.index(rule[0]) > line.index(rule[1]):
                        good_line = False
    if good_line is True:
        good_lines.append(line)

bad_lines = []
for line in full_prints:
    if line not in good_lines:
        bad_lines.append(line)


fixed_lines = []
for line in bad_lines:
    for num in line:
        for rule in full_rules:
            if num == rule[0]:
                if rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                    moved = rule[1]
                    line.pop(line.index(rule[1]))
                    line.append(moved)
    for num in line:
        for rule in full_rules:
            if num == rule[0]:
                if rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                    moved = rule[1]
                    line.pop(line.index(rule[1]))
                    line.append(moved)
    for num in line:
        for rule in full_rules:
            if num == rule[0]:
                if rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                    moved = rule[1]
                    line.pop(line.index(rule[1]))
                    line.append(moved)

    fixed_lines.append(line)

total = 0
for line in fixed_lines:
    middle = (len(line)-1)/2
    total += line[int(middle)]


print(total)
