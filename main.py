import requests
import datetime
from colorama import Fore
import threading

global count
count = 0

file = input('Enter name of file with proxies: ')

if '.txt' in file:
    ofile = file
else:
    ofile = file + '.txt'

with open(ofile,'r') as proxyfile:
    proxies = proxyfile.readlines()
    amount = len(proxies)

print(Fore.CYAN + 'Checking proxies....')

def check_proxies(proxy,amount):
    global count
    proxy = proxy.strip()
    proxyDict = { 
        "https" : proxy
    }
    start = datetime.datetime.now()
    try:

        # timeout = 1 limits proxies to under 1000 ms, if you want a higher or lower threshold, change this number
        # url can be changed to test proxies on different sites

        res = requests.get(url='https://google.com',proxies=proxyDict,timeout=1)
        if res.status_code == 200:
            end = datetime.datetime.now()
            raw_speed = str(end-start).split('.')[1]
            speed_int = round(int(raw_speed),2)
            speed = round(speed_int/1000)

            #print working proxies and their speed

            proxy_info = f'{proxy} - {speed}ms - {count}/{amount}'
            print(Fore.GREEN + proxy_info)
            count += 1

    except:
        count += 1
        # to see failed proxies, remove the pound symbol from the following line
        #print(Fore.RED + f'{proxy} - Failed - {count}/{amount}')
        pass

# begin checking proxies

for proxy in proxies:
    threading.Thread(target=check_proxies(proxy,amount))

