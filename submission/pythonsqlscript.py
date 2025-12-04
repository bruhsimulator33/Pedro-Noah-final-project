# number 1 
#!/usr/bin/python

# Filename to read
filename = 'gdp_clean.csv'

# Table to place data into
tableName = 'gdp'

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
# format for each column design is [IS_STR, TYPE, NULL OR NOT NULL]
default = [1, 'VARCHAR(64)', 'NULL']

for i in range(len(headers)):
    design[i] = default

# Redefine types for numeric columns
# Country is string, year and total_gdp_million are numeric
design[1] = [0, 'INT', 'NULL']  # year
design[2] = [0, 'FLOAT', 'NULL']  # total_gdp_million

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
        # NULL if value is missing, quotes for strings, value for numbers
        if row[index] == '':
            insert.append('NULL')
        elif design[index][0]:
            # Escape single quotes in strings
            row[index] = row[index].replace("'", "\\'")
            insert.append("'" + str(row[index]) + "'")
        else:
            insert.append(str(row[index]))
    print('INSERT INTO', tableName, 'VALUES (', ','.join(insert), ');')

#number 2
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

#number 3
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