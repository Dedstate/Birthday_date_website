import csv

current = []
with open("birthdays.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for index, row in enumerate(reader):
        current.append(tuple(row))

archived = []
with open("birthdays_archived.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for index, row in enumerate(reader):
        archived.append(tuple(row))
