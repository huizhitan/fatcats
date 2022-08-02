

import csv
from pathlib import Path
filepath = Path.cwd()/'csv_reports'/'overheads-day-90.csv'

read = filepath.open(mode = 'r', encoding = 'UTF-8', newline = '')
next(read)
reader = read.readlines()
data = list(reader)
for maxdata in range(1):
    maxdata = float(data[2])
    print(max(maxdata))
    break
       

        