import csv
import pandas as pd
import sys

filename = str(sys.argv[1])

with open(filename, newline='') as csvfile:
    columnName = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in columnName:
        print(row)
