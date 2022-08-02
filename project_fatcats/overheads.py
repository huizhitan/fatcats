

import csv
from pathlib import Path
filepath = Path.cwd()/'csv_reports'/'overheads-day-90.csv'
def overheads_funtion():
    read = filepath.open(mode = 'r', encoding = 'UTF-8', newline = '')
    next(read)
    reader = read.readlines()
    data = list(reader)
    for maxdata in range(0):
        floating = float(maxdata)
        print(floating)
        break
        overheads_function()

        