#!/usr/bin/python

# Filename to read
filename = 'olympics_clean.csv'

# Table to place data into
tableName = 'olympics'

# auto generate table design
design = {}
import csv

# Read CSV
with open(filename) as f:
    data = f.readlines()

# Retrieve header row
headers = data[0].strip().split(',')
headers = [name.replace(" ","_") for name in headers]  #replace spaces with _
headers = [name.replace("-","_") for name in headers]  #replace - with _

# Default type for each column in our table.
default = [1, 'VARCHAR(64)', 'NULL']

for i in range(len(headers)):
    design[i] = default

# Redefine types for numeric columns
design[1] = [0, 'INT', 'NULL']  # Year is numeric

# Create the CREATE TABLE statement
print('DROP TABLE IF EXISTS', tableName, ';')
print('CREATE TABLE', tableName, '(')
create = []
maxSize = [10,10]
for i in range(len(headers)):
    maxSize[0] = max(maxSize[0], len(headers[i])+2)
    maxSize[1] = max(maxSize[1], len(design[i][1])+2)
for i in range(len(headers)):
    create.append(" ".join([headers[i].ljust(maxSize[0]), design[i][1].ljust(maxSize[1]), design[i][2]]))
print(' ', ",\n  ".join(create))
print(");")

# Generate INSERT statements
for row in csv.reader(data[1:], quotechar='"', delimiter=',', skipinitialspace=True):
    insert = []
    for index in range(len(headers)):

        if headers[index].lower() == 'country':
            row[index] = row[index].upper() #try this out to make all the countries upper case

        if row[index] == '':
            insert.append('NULL')
        elif design[index][0]:
            row[index] = row[index].replace("'", "\\'")
            insert.append("'" + str(row[index]) + "'")
        else:
            insert.append(str(row[index]))
    print('INSERT INTO', tableName, 'VALUES (', ','.join(insert), ');')