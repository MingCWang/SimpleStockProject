import sys
import os
from datetime import datetime
from Class.PL import ProfitLoss 

today = datetime.today()
currentdate = today.strftime('%Y-%m-%d %H:%M:%S')

# Show defined variables
price = [] 
lowprice = []
upprice = []
units = []
date = []
id = []
choice = []
stock = []
Taiwan = '.tw'

# Two fuctions deletedata() and savedata()
def deletedata():
    print()
    choice = input('THIS WILL DELETE ALL DATAS ENTER [YES] TO CONFIRM ELSE ENTER [NO]: ')
    choice = choice.upper()
    print()
    if choice == 'YES':
        try:
            os.path.exists('/Users/TheSky/Desktop/Python/SimpleStockProject/mydata.txt')
            os.remove('/Users/TheSky/Desktop/Python/SimpleStockProject/mydata.txt')
            print('[mydata.txt] file deleted \n')
        except:
            print('No existing datas yet! \n')
    else:
        print()

#Save data to 'mydata.txt'
def savedata(): 
    f = open('mydata.txt', 'a+')
    for i in range (0, len(price)):
        PL = ProfitLoss(upprice[i], lowprice[i], price[i], units[i])
        currentH = upprice[i] * units[i]
        currentL = lowprice[i] * units[i]
        id.append(i)
        date.append(currentdate)
        f.write('\n')
        f.write('=============================== {} =================================='.format(date[i]))
        f.write('\n')
        f.write('{}{}'.format(stock, Taiwan))
        f.write('\n')
        f.write('You bought %d (TWD)' % PL.Buy())
        f.write('\n\n')
        f.write('If sold at {} (TWD)\n'.format(currentH))
        f.write('Profit Percentage = %.3f %% \n' % (PL.profitper()))
        f.write('Profit [Selled stocks at high] = %.f \n' % (PL.Profit()))
        f.write('\n')
        f.write('If sold at {} (TWD)\n'.format(currentL))
        f.write('Loss Percentage = %.3f %% \n' % (PL.lossper()))
        f.write('Loss [Selled stocks at low] = %.f \n' % (PL.Loss()))
        f.write('======================================================================================')
        f.write('\n')
    f.close()
    print()
    print('DATA SAVED TO "mydata.txt"')
    print()

print()
print('Simple Stock Profit Calculations')
print()

# main code below
while True:
    decision = input('[B] BUY STOCKS, [E] END, [D] DELETE DATA: ')
    print()
    decision = decision.upper()
    if decision == 'B':
        decision2 = input('[O] ODD-LOT ORDERS (below 1000 shares), [N] NORMAL (1 = 1000 shares): ')
        print()
        decision2 = decision2.upper()
        stock = input('Enter the company number: ')
        print()
        while True:
            myprice = input('Insert buying price: ')
            price.append(float(myprice))
            print()
            if decision2 == 'O':
                Units = input('Insert buying units: ')
                units.append(int(float(Units)))
            elif decision2 == 'N':
                Units = int(float(input('Insert buying units (1 = 1000 shares): ')))
                Units *= 1000
                units.append(Units)
            else: 
                print('[error] try again\n')
                break
            print()
            lastlowestprice = (input('Insert the last lowest price: '))
            lowprice.append(float(lastlowestprice))
            print()
            lasthighestprice = (input('Insert the last highest price: '))
            print()
            upprice.append(float(lasthighestprice))
            break
    elif decision == 'E':
        decision3 = input('[S] SAVE DATA, [D] DELETE DATA: ')
        decision3 = decision3.upper()
        if decision3 == 'S':
            savedata()
            sys.exit("Ended system")
        elif decision3 == 'D':
            deletedata()
            sys.exit("Ended system")
    elif decision == 'D':
        deletedata()
    else: 
        print('[error] try again')
        print()
