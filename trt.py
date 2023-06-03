import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')

import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 'BMH' and password == 'CYBER':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')

bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] Join Over Facebook Group {white}')
    os.system('xdg-open https://www.facebook.com/AungZinMin.2006//')
    time.sleep(0.05)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
