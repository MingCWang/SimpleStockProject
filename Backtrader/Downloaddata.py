import requests
from datetime import datetime

today = datetime.today()
currentdate = today.strftime('%Y-%m-%d %H:%M:%S')
url = 'https://query1.finance.yahoo.com/v7/finance/download/6282.TW?period1=1572965220&period2=1604587620&interval=1d&events=history&includeAdjustedClose=true'


class getdata():
    print()
    response = requests.get(url, allow_redirects=True)

    if response.status_code != 200:
        print('Failed to get data: ', response.status_code)
    else:
        f = open('6282.csv', 'w')
        f.write(response.text)
        print(currentdate, 'DATA REFRESHED')
        f.close()
    print()
