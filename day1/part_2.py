import csv

loc_list_1 = []
loc_list_2 = []
file = open('locations.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.DictReader(file)

for col in csv_reader:
    loc_list_1.append(int(col['list_1']))
    loc_list_2.append(int(col['list_2']))
file.close()
loc_list_1.sort()
loc_list_2.sort()

similarity = 0
for num1 in loc_list_1:
    count = 0
    for num2 in loc_list_2:
        if num1 == num2:
            count += 1
    similarity += (num1 * count)

print(similarity)
