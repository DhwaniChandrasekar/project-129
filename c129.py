import csv
import pandas as pd

data1 = []
data2 = []

with open("bright_stars.csv",'r') as rea:
    csvReader = csv.reader(rea)
    for i in csvReader:
        data1.append(i)

with open("dwarf_stars.csv",'r') as rea:
    csvReader = csv.reader(rea)
    for i in csvReader:
        data2.append(i)

headers1 = data1[0]
headers2 = data2[0]
sdata1 = data1[1:]
sdata2 = data2[1:]

headers = headers1 + headers2
starsdata = []

for i in sdata1:
    starsdata.append(i)

for i in sdata2:
    starsdata.append(i)


with open("output129.csv",'w') as data: #make a new csv file
    csvWriter = csv.writer(data)
    csvWriter.writerow(headers)
    csvWriter.writerows(starsdata)

