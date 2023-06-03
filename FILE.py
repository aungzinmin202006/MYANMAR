import os, platform, time, sys

try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')

import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 'BMH2' and password == 'CYBER':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')

bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')
 import FILE64
elif bit == '32bit':
 print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')
 import FILE32
