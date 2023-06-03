import os
os.system('xdg-open https://www.facebook.com/AungZinMin.2006')
#Ase Kia Dekh raha Bhai
#32bit/64bit run krne ka new method he

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

try:
 import TestV1
except:
 try:
  import TestV2
 except:
  print('Thanks For Using Tool<3')
