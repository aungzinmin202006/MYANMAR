import os,platform
os.system('xdg-open https://www.facebook.com/AungZinMin.2006')
os.system('pip uninstall requests')
os.system('pip install requests')

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

BXI=platform.architecture()[0]
if BXI=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof")
