def coh_function(x):

    import csv

    with open('csv_reports\cash-on-hand-usd.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
       

    increase= True
    for i in range(1,len(data)-1):
        if int(data[i+1][1])<int(data[i][1]):
            increase = False
            deficit = int(data[i][1])- int(data[i+1][1])
            print('[CASH DEFICIT] DAY: '+data[i+1][0]+', AMOUNT: SGD'+str(deficit/x))
    if increase: 
        print('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')