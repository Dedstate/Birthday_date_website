import csv

a = []
with open("birthdays.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for index, row in enumerate(reader):
        a.append(tuple(row))
