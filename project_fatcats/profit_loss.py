
def profitloss_function(x):
    import csv

    with open('csv_reports\profit-and-loss.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
       
    x=1.5
    increase= True
    for p in range(1,len(data)-1):
        if int(data[p+1][1])<int(data[p][1]):
            increase = False
            deficit = int(data[p][1])- int(data[p+1][1])
            print('[PROFIT DEFICIT] DAY: '+data[p+1][0]+', AMOUNT: SGD'+str(deficit/x))
    if increase: 
        print('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
