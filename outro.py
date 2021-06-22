import csv

usa = "United States"

with open('new.csv', 'rt') as rf:
    reader = csv.reader(rf, delimiter=',')
    with open('b.csv', 'w') as wf:
        writer = csv.writer(wf)    
        for row in reader:
            newrow = row[3]
            if usa in row[3]:
                row[3] = " "
            writer.writerow(row)