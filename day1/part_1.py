import csv

loc_list_1 = []
loc_list_2 = []
file = open("locations.csv", "r", encoding="utf-8-sig")
csv_reader = csv.DictReader(file)

for col in csv_reader:
    loc_list_1.append(int(col["list_1"]))
    loc_list_2.append(int(col["list_2"]))
file.close()
loc_list_1.sort()
loc_list_2.sort()

distances = []
i = 0
for num in loc_list_1:
    distances.append(abs(num - loc_list_2[i]))
    i += 1

total = sum(distances)
print(total)
