#!/usr/bin/python

import csv

# Filename to read
filename = 'inflation_clean.csv'

# Table to place data into
tableName = 'inflation'

# Read CSV and parse header correctly using csv.reader
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, quotechar='"')
    headers = next(reader)  # first row is the header
    headers = [h.replace(" ", "_").replace("-", "_") for h in headers]

# Auto-generate table design
design = {}
# Default type: string
default = [1, 'VARCHAR(64)', 'NULL']

for i in range(len(headers)):
    design[i] = default

# Define types for known numeric columns
# Adjust these indexes based on actual CSV order
# From your CSV:
# 0-country, 1-year, 2-inflation, 3-real_interest, 4-lending_interest, 5-unemployment, 6-incomeLevel
design[1] = [0, 'INT', 'NULL']
design[2] = [0, 'FLOAT', 'NULL']
design[3] = [0, 'FLOAT', 'NULL']
design[4] = [0, 'FLOAT', 'NULL']
design[5] = [0, 'FLOAT', 'NULL']

# CREATE TABLE statement
print(f'DROP TABLE IF EXISTS {tableName};')
print(f'CREATE TABLE {tableName} (')
create = []
maxSize = [10, 10]
for i in range(len(headers)):
    maxSize[0] = max(maxSize[0], len(headers[i]) + 2)
    maxSize[1] = max(maxSize[1], len(design[i][1]) + 2)
for i in range(len(headers)):
    create.append(" ".join([headers[i].ljust(maxSize[0]), design[i][1].ljust(maxSize[1]), design[i][2]]))
print('  ' + ",\n  ".join(create))
print(");")

# INSERT statements
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, quotechar='"')
    next(reader)  # skip header
    for row in reader:
        insert = []
        for index in design:
            if index >= len(row) or row[index] == '':
                insert.append('NULL')
            elif design[index][0]:  # string
                val = row[index].replace("'", "\\'")
                insert.append(f"'{val}'")
            else:  # number
                insert.append(str(row[index]))
        print(f'INSERT INTO {tableName} VALUES ({",".join(insert)});')