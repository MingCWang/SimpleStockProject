import sys
import os
from datetime import datetime
from Class.PL import Percentage, ProfitLoss 
today = datetime.today()
currentdate = today.strftime('%Y-%m-%d %H:%M:%S')

print()
print('Risk Mangement'.upper(), ('6282.tw'))
print()

price = [] # Show defined variables
lowprice = []
upprice = []
units = []
date = []
id = []
choice = []




def savedata(): #Save data to 'mydata.txt'
    f = open('mydata.txt', 'a')
    #f.write('SWING TRADING HISTORY \n')
    for i in range (0, len(price)):
        per = Percentage(upprice[i], lowprice[i], price[i])
        PL = ProfitLoss(upprice[i], lowprice[i], price[i], units[i])
        joinedtuple = (price[i], lowprice[i], upprice[i], units[i])
        id.append(i)
        date.append(currentdate)
        f.write('\n')
        f.write('=============================== {} =================================='.format(date[i]))
        f.write('\n')
        f.write('Buy, Low, High, Units')
        f.write('\n')
        f.write(str(joinedtuple))
        f.write('\n\n')
        f.write('Profit Percentage = %.3f %% \n' % (per.profit()))
        f.write('Loss Percentage = %.3f %% \n' % (per.loss()))
        f.write('Profit [Selled stocks at high] = %.f \n' % (PL.Profit()))
        f.write('Loss [Selled stocks at low] = %.f \n' % (PL.Loss()))
        f.write('=====================================================================')
        f.write('\n')
    f.close()
    print('DATA SAVED')


def printdata():
    print('SWING TRADING HISTORY \n')
    for i in range(0, len(price)):
        per = Percentage(upprice[i], lowprice[i], price[i])
        PL = ProfitLoss(upprice[i], lowprice[i], price[i], units[i])
        joinedtuple = (price[i], lowprice[i], upprice[i], units[i])
        date.append(currentdate)
        id.append(i)
        print('\n')
        print('=============================== {} =================================='.format(id[i] + 1))
        print('Datetime: ', date[i], '\n')
        print('Buy, Low, High, Units')
        print(joinedtuple)
        print('\nProfit Percentage = %.3f %% \n' % (per.profit()))
        print('Loss Percentage = %.3f %% \n' % (per.loss()))
        print('Profit [Selled stocks at high] = %.f \n' % (PL.Profit()))
        print('Loss [Selled stocks at low] = %.f' % (PL.Loss()))
        print('=====================================================================')

while True:
    decision = input('[B] BUY STOCKS, [O] OPEN PURCHASE HISTORY, [S] SAVE DATA, [E] END, [D] DELETE DATA: ')
    print()
    decision = decision.upper()
    if decision == 'B':
        while True:
            myprice = input('Insert buying price: ')
            price.append(float(myprice))
            print()
            Units = (input('Insert buying units: '))
            units.append(int(float(Units)))
            print()
            lastlowestprice = (input('Insert the last lowest price: '))
            lowprice.append(float(lastlowestprice))
            print()
            lasthighestprice = (input('Insert the last highest price:'))
            print()
            upprice.append(float(lasthighestprice))
            break

    elif decision == 'O':
        printdata()
        flag = 0
        while (flag == 0):
            decision2 = input('[C] CONTINUE, [E] END: ')
            decision2 = decision2.upper()
            if decision2 == 'C':
                print()
                flag += 1
                continue
            elif decision2 == 'E':
                sys.exit("Ended system")
            else:
                print('[error] try again')
                continue 
    elif decision == 'S':
        savedata()
    elif decision == 'E':
        sys.exit("Ended system")
    elif decision == 'D':
        choice = input('THIS WILL DELETE ALL DATAS ENTER [YES] TO CONFIRM ELSE ENTER [NO]: ')
        if choice == 'YES':
            os.remove('/Users/TheSky/Desktop/Python/Stockrecords/mydata.txt')
        else 
            continue
    else: 
        print('[error] try again')
        continue

 