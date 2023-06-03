import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')


print('username is:\033[0;92mBMH6')
      
import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    yourkey  = input(' \033[0;93mEnter Your Key: ')

    if username == 'BMH6' and yourkey == '3929djxid_ieyour':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect key and username Please Trying ')
        attemps += 1
        continue


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
