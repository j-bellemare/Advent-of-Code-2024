inpute_file = open("./inputs/unusual_data.txt", "r")

report_status = 0

for line in inpute_file:
    report = line.split()
    report = [int(x) for x in report]

    start_num = report[0]
    report.pop(0)
    status = True
    prev_num = start_num
    prob_limit = 0
    for num in report:
        if report[0] > start_num:
            if num > prev_num and num - prev_num < 4 and status is True:
                status = True
                prev_num = num
            else:
                prob_limit += 1
                if prob_limit > 1:
                    status = False

        elif report[0] < start_num:
            if num < prev_num and prev_num - num < 4 and status is True:
                status = True
                prev_num = num
            else:
                prob_limit += 1
                if prob_limit > 1:
                    status = False

        else:
            prob_limit += 1
            if prob_limit > 4:
                status = False

    if status is True:
        report_status += 1

print(report_status)
