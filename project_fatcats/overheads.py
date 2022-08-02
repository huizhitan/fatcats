
def overheads_funtion(x):
    import csv

    with open('csv_reports\overheads-day-90.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    for p in range(1,len(data)-1):
        if float(data[p+1][1])<float(data[p][1]):
            print('[HIGHEST OVERHEADS] DAY: '+data[p+1][0]+', AMOUNT: SGD'+float(data[p+1][1]/x))


    #for maxdata in data:
        #print(maxdata)




        #floating = float(maxdata)
        #print(floating)
        #break


overheads_funtion(1.5)

        