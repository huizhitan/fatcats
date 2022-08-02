def coh_function(f):

    import csv

    with open('csv_reports\cash-on-hand-usd.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
       

    increase= True
    for c in range(1,len(data)-1):
        if int(data[c+1][1])<int(data[c][1]):
            increase = False
            deficit = int(data[c][1])- int(data[c+1][1])
            print('[CASH DEFICIT] DAY: '+data[c+1][0]+', AMOUNT: SGD'+str(deficit/x))
    if increase: 
        print('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')