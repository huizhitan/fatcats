def overhead_function(x):
    import csv

    with open('csv_reports/overheads-day-90.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    
    highest = 1
    for p in range(1,len(data)-2):
        if float(data[p+1][1])>float(data[highest][1]):
            highest = p+1
            
    print('[HIGHEST OVERHEADS] DAY: '+data[highest][0]+', AMOUNT: SGD'+str(float(data[highest][1])*x))

        