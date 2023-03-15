import csv

result = ''
with open('t2-l10-d4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            result+=(f'\t{"{"}x: {row[0]}, y:{row[1]}, status: false, {"}"},\n')
            line_count += 1
    print(f'Processed {line_count} lines.')
f = open("output.txt", "w")
f.write(result)
f.close()
