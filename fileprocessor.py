import csv

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        line_count += 1
        if line_count == 5:
            break;
    print('Lines are printed')
